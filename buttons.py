from gpiozero import Button, LED
import time

# Button objects
left_button = gpiozero.Button(17)
up_button = gpiozero.Button(27)
right_button = gpiozero.Button(22)
down_button = gpiozero.Button(5)
center_button = gpiozero.Button(6)
demo_button = gpiozero.Button(26)

# LED objects
left_led = gpiozero.LED(25)
up_led = gpiozero.LED(8)
right_led = gpiozero.LED(7)
down_led = gpiozero.LED(1)
center_led = gpiozero.LED(12)