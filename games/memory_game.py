# sudo apt-get install python-rpi.gpio python3-rpi.gpio
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
# TODO: setup 3 more input pins for button press signal
# TODO: setup 4 output pins to control button LED

import random

def generate_sequence(length=5):
    directions = ["up", "down", "left", "right"]
    return [random.choice(directions) for _ in range(length)]

def start_game():
    print("Starting Memory Game...")
    # TODO: tell user to prepare for memory game
    sequence = generate_sequence()
    while True:
        for i in range(len(sequence)):
            for direction in sequence[0:i]:
                # TODO: light up appropriate button
                # TODO: wait for input, continue if correct, start over if incorrect
                pass

def stop_game():
    print("Stopping Memory Game...")
    pass