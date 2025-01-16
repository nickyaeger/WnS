# pip install pyserial
# pip install adafruit-circuitpython-bno08x-rvc
# sudo apt-get install python-rpi.gpio python3-rpi.gpio

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # left press
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # up press
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # right press
GPIO.setup(28, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # down press

GPIO.setup(11, GPIO.OUT) # left LED
GPIO.setup(13, GPIO.OUT) # up LED
GPIO.setup(15, GPIO.OUT) # right LED
GPIO.setup(29, GPIO.OUT) # down LED

import random, time

import serial
uart = serial.Serial("/dev/ttyS0", 115200)

from adafruit_bno08x_rvc import BNO08x_RVC
rvc = BNO08x_RVC(uart)

def generate_sequence(length=10):
    directions = ["up", "down", "left", "right"]
    return [random.choice(directions) for _ in range(length)]

def direction_to_pin(direction):
    if direction == "left":
        return 11
    elif direction == "up":
        return 13
    elif direction == "right":
        return 15
    elif direction == "down":
        return 29
    else:
        print("Invalid direction")
        return None

def read_imu_direction(threshold=50):
    yaw, pitch, roll, x_accel, y_accel, z_accel = rvc.heading
    if pitch < -threshold:
        return "up"
    elif pitch > threshold:
        return "down"
    elif roll < -threshold:
        return "left"
    elif roll > threshold:
        return "right"
    else:
        return None

def start_game(time_limit=1):
    print("Starting Wake'n'Shake Game...")
    sequence = generate_sequence()
    while True:
        for direction in sequence:
            pin = direction_to_pin(direction)
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.5)

            start_time = time.time()
            while time.time() - start_time <= time_limit:
                detected_direction = read_imu_direction()
                if detected_direction == direction:
                    print(f"{direction.capitalize()} detected!")
                    break
            else:
                print("Time's up or incorrect movement! Game over.")
                # TODO: wrong buzzer sound, wait one second before restarting
                break
        else:
            print("Congratulations! You completed the sequence!")
            # TODO: success sound, stop alarm
            break

def stop_game():
    print("Stopping Wake'n'Shake Game...")

# test code
while True:
    yaw, pitch, roll, x_accel, y_accel, z_accel = rvc.heading
#    print("Yaw: %2.2f Pitch: %2.2f Roll: %2.2f Degrees" % (yaw, pitch, roll))
#    print("Acceleration X: %2.2f Y: %2.2f Z: %2.2f m/s^2" % (x_accel, y_accel, z_accel))
    if pitch > 50:
        print("down")
    elif pitch < -50:
        print("up")
    elif roll > 50:
        print("right")
    elif roll < -50:
        print("left")