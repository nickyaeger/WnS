import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BOARD)  # Use Broadcom pin numbering

# Button pins
left_button = 18
up_button = 22
right_button = 24
down_button = 26
# center_button = 16
# demo_button = 26

# LED pins
left_led = 3
up_led = 5
right_led = 11
down_led = 13
# center_led = 6

# Set up buttons as inputs with pull-up resistors
GPIO.setup(left_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(up_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(right_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(down_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(center_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(demo_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up LEDs as outputs
GPIO.setup(left_led, GPIO.OUT)
GPIO.setup(up_led, GPIO.OUT)
GPIO.setup(right_led, GPIO.OUT)
GPIO.setup(down_led, GPIO.OUT)
# GPIO.setup(center_led, GPIO.OUT)

def get_button_input():
    # Check each button and control corresponding LED
    if not GPIO.input(left_button):  # Button is pressed (low signal)
        print("left")
        GPIO.output(left_led, GPIO.HIGH)  # Turn on LED
    else:
        GPIO.output(left_led, GPIO.LOW)   # Turn off LED

    if not GPIO.input(up_button):
        print("up")
        GPIO.output(up_led, GPIO.HIGH)
    else:
        GPIO.output(up_led, GPIO.LOW)

    if not GPIO.input(right_button):
        print("right")
        GPIO.output(right_led, GPIO.HIGH)
    else:
        GPIO.output(right_led, GPIO.LOW)

    if not GPIO.input(down_button):
        print("down")
        GPIO.output(down_led, GPIO.HIGH)
    else:
        GPIO.output(down_led, GPIO.LOW)

#    if not GPIO.input(center_button):
#        print("center")
#        GPIO.output(center_led, GPIO.HIGH)
#    else:
#        GPIO.output(center_led, GPIO.LOW)
#
#    if not GPIO.input(demo_button):
#        print("demo")

try:
    while True:
        get_button_input()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Exiting program...")
finally:
    GPIO.cleanup()  # Reset GPIO pins to a safe state
