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
# import keyboard # for testing

def generate_sequence(length=5):
    directions = ["up", "down", "left", "right"]
    return [random.choice(directions) for _ in range(length)]

def direction_to_pin(direction):
    if direction == "left":
        print("memorize left")
        return 11
    elif direction == "up":
        print("memorize up")
        return 13
    elif direction == "right":
        print("memorize right")
        return 15
    elif direction == "down":
        print("memorize down")
        return 29
    else:
        print("Invalid direction")
        return None
    

def read_button_press():
    if GPIO.input(22):
    # if keyboard.is_pressed('a'):
        print("Left button pressed")
        return "left"
    elif GPIO.input(24):
    # elif keyboard.is_pressed('w'):
        print("Up button pressed")
        return "up"
    elif GPIO.input(26):
    # elif keyboard.is_pressed('d'):
        print("Right button pressed")
        return "right"
    elif GPIO.input(28):
    # elif keyboard.is_pressed('s'):
        print("Down button pressed")
        return "down"
    else:
        return None

def start_game():
    print("Starting Memory Game...")
    sequence = generate_sequence()
    while True:
        success = True
        for i in range(len(sequence)):
            # Display part of sequence to be memorized
            for direction in sequence[0:i+1]:
                # print(direction)
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
                        print("Correct direction " + str(i))
                        num_pressed += 1
                        while read_button_press():
                            continue
                    else:
                        print("Incorrect direction " + str(i))
                        success = False
                        while read_button_press():
                            continue
                        break
            if not success:
                print("Restarting memory game")
                break
        if success:
            print("Completed memory game")
            break

def stop_game():
    print("Stopping Memory Game...")
    pass