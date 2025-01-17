from gpiozero import Button, LED
import time

# Button objects
left = Button(17)
up = Button(27)
right = Button(22)
down = Button(5)
center = Button(6)
demo = Button(26)

# LED objects
left_led = LED(25)
up_led = LED(8)
right_led = LED(7)
down_led = LED(1)
center_led = LED(12)

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
