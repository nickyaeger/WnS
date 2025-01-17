from gpiozero import Button, LED
import time

# Button objects
left = Button(25)
up = Button(8)
right = Button(7)
down = Button(12)
center = Button(16)
demo = Button(26)

# LED objects
left_led = LED(17)
up_led = LED(27)
right_led = LED(22)
down_led = LED(5)
center_led = LED(6)

def get_button_input():
    if left.is_pressed:
        print("left")
        left_led.on()
    else:
        left_led.off()

    if up.is_pressed:
        print("up")
        up_led.on()
    else:
        up_led.off()

    if right.is_pressed:
        print("right")
        right_led.on()
    else:
        right_led.off()

    if down.is_pressed:
        print("down")
        down_led.on()
    else:
        down_led.off()

    if center.is_pressed:
        print("center")
        center_led.on()
    else:
        center_led.off()

    if demo.is_pressed:
        print("demo")

while True:
    get_button_input()
    time.sleep(0.1)
