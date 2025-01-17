# sudo apt-get install python-rpi.gpio python3-rpi.gpio
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # left press
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # up press
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # right press
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # down press

GPIO.setup(3, GPIO.OUT) # left LED
GPIO.setup(5, GPIO.OUT) # up LED
GPIO.setup(11, GPIO.OUT) # right LED
GPIO.setup(13, GPIO.OUT) # down LED

import random, time
# import keyboard # for testing

def generate_sequence(length=10):
    directions = ["up", "down", "left", "right"]
    return [random.choice(directions) for _ in range(length)]

def direction_to_pin(direction):
    if direction == "left":
        return 3
    elif direction == "up":
        return 5
    elif direction == "right":
        return 11
    elif direction == "down":
        return 13
    else:
        print("Invalid direction")
        return None
    
def read_button_press():
    if GPIO.input(18):
    # if keyboard.is_pressed('a'):
        # print("Left button pressed")
        return "left"
    elif GPIO.input(22):
    # elif keyboard.is_pressed('w'):
        # print("Up button pressed")
        return "up"
    elif GPIO.input(24):
    # elif keyboard.is_pressed('d'):
        # print("Right button pressed")
        return "right"
    elif GPIO.input(26):
    # elif keyboard.is_pressed('s'):
        # print("Down button pressed")
        return "down"
    else:
        return None

def start_game(time_limit=1):
    print("Starting Whackamole...")
    while True:
        sequence = generate_sequence()
        GPIO.output(3, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        for direction in sequence:
            print(direction)
            pin = direction_to_pin(direction)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(pin, GPIO.HIGH)

            start_time = time.time()
            while time.time() - start_time <= time_limit:
                detected_direction = read_button_press()
                if detected_direction == direction:
                    print(f"{direction.capitalize()} detected!")
                    while read_button_press():
                            continue
                    GPIO.output(pin, GPIO.LOW)
                    break
            else:
                print("Time's up or incorrect movement! Game over.")
                GPIO.output(pin, GPIO.LOW)
                # TODO: wrong buzzer sound
                break
        else:
            print("Congratulations! You completed the sequence!")
            GPIO.output(pin, GPIO.LOW)
            # TODO: success sound, stop alarm
            break
    pass

def stop_game():
    print("Stopping Whackamole..")
    pass