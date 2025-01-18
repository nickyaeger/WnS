import RPi.GPIO as GPIO
import time

class Buttons:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        # Button pins
        self.button_pins = {
            "left": 18,
            "up": 22,
            "right": 24,
            "down": 26,
            "center": 36,
            #"demo": 26,
        }

        # LED pins
        self.led_pins = {
            "left": 3,
            "up": 5,
            "right": 11,
            "down": 13,
            "center": 31,
        }

        # Set up buttons as inputs with pull-down resistors
        for pin in self.button_pins.values():
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # Set up LEDs as outputs
        for pin in self.led_pins.values():
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

    def get_pressed_button(self):
        """Check if any button is pressed and return its name."""
        for name, pin in self.button_pins.items():
            if GPIO.input(pin) == GPIO.HIGH:
                return name
        return None

    def light_up_led(self, button_name):
        """Light up the LED corresponding to the button."""
        if button_name in self.led_pins:
            GPIO.output(self.led_pins[button_name], GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(self.led_pins[button_name], GPIO.LOW)

    def cleanup(self):
        """Clean up GPIO pins."""
        GPIO.cleanup()


# Instantiate the Buttons class for standalone testing
if __name__ == "__main__":
    buttons = Buttons()
    try:
        print("Press buttons to test. Press Ctrl+C to exit.")
        while True:
            button = buttons.get_pressed_button()
            if button:
                print(f"{button} button pressed")
                buttons.light_up_led(button)
            while buttons.get_pressed_button():
                continue
    except KeyboardInterrupt:
        print("Exiting program...")
    finally:
        buttons.cleanup()
