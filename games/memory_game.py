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

import sounds

def generate_sequence(length=5):
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

def start_game():
    print("Starting Memory Game...")
    sounds.playMemory()
    while True:
        sequence = generate_sequence()
        GPIO.output(3, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        success = True
        for i in range(len(sequence)):
            # Display part of sequence to be memorized
            for direction in sequence[0:i+1]:
                print(direction)
                pin = direction_to_pin(direction)
                GPIO.output(pin, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(pin, GPIO.LOW)
                time.sleep(0.5)
            num_pressed = 0
            while num_pressed < i+1:
                pressed = read_button_press()
                if pressed:
                    if pressed == sequence[num_pressed]:
                        print("Correct direction " + sequence[num_pressed])
                        num_pressed += 1
                        while read_button_press():
                            continue
                    else:
                        print("Incorrect direction " + sequence[num_pressed])
                        success = False
                        while read_button_press():
                            continue
                        break
                    time.sleep(1)
            if not success:
                print("Restarting memory game")
                time.sleep(3)
                break
        if success:
            print("Completed memory game")
            break

def stop_game():
    print("Stopping Memory Game...")
    pass