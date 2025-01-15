# pip install pyserial
# pip install adafruit-circuitpython-bno08x-rvc

import serial
uart = serial.Serial("/dev/serial0", 115200)

from adafruit_bno08x_rvc import BNO08x_RVC
rvc = BNO08x_RVC(uart)

# yaw, pitch, roll, x_accel, y_accel, z_accel = rvc.heading
# print("Yaw: %2.2f Pitch: %2.2f Roll: %2.2f Degrees" % (yaw, pitch, roll))
# print("Acceleration X: %2.2f Y: %2.2f Z: %2.2f m/s^2" % (x_accel, y_accel, z_accel))

import random, time

def generate_sequence(length=10):
    directions = ["up", "down", "left", "right"]
    return [random.choice(directions) for _ in range(length)]

def read_imu_direction(threshold=1.0):
    yaw, pitch, roll, x_accel, y_accel, z_accel = rvc.heading
    if y_accel > threshold:
        return "up"
    elif x_accel > threshold:
        return "right"
    elif y_accel < -threshold:
        return "down"
    elif x_accel < -threshold:
        return "left"
    else:
        return None

def play_shake(time_limit=1):
    sequence = generate_sequence()
    while True:
        for direction in sequence:
            start_time = time.time()
            while time.time() - start_time <= time_limit:
                detected_direction = read_imu_direction()
                if detected_direction == direction:
                    print(f"{direction.capitalize()} detected!")
                    break
            else:
                print("Time's up or incorrect movement! Game over.")
                break
        else:
            print("Congratulations! You completed the sequence!")
            break