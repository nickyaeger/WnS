# pip install pyserial
# pip install adafruit-circuitpython-bno08x-rvc

import random, time

import serial
uart = serial.Serial("/dev/ttyS0", 115200)

from adafruit_bno08x_rvc import BNO08x_RVC
rvc = BNO08x_RVC(uart)

def generate_sequence(length=10):
    directions = ["up", "down", "left", "right"]
    return [random.choice(directions) for _ in range(length)]

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
    # TODO: tell user to prepare for wake'n'shake
    sequence = generate_sequence()
    while True:
        for direction in sequence:
            # TODO: light up appropriate button
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