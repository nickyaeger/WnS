"""Contains the Clock class."""

import time

class Clock():
    """Stores user configurations and what is shown on the LED display."""
    def __init__(self) -> None:
        # Display values
        self.char0 = str(1)
        self.char1 = str(2)
        self.char2 = str(0)
        self.char3 = str(0)
        self.colon = True
        self.led0 = False
        self.led1 = False
        self.led2 = False
        self.led3 = False

        # Configurations
        self._24hour = True

    def update(self, text: str, colon: bool, leds: list) -> None:
        """Updates the display with the given text, colon, and LEDs.

        Parameters
        ----------
        text : str
            The text to display. Must be 4 characters long.
        colon : bool
            Whether to display the colon.
        leds : list
            The boolean state of each LED. Must be 4 elements long.
        """
        if len(text) != 4:
            raise ValueError("Text must be 4 characters long")
        self.char0 = text[0]
        self.char1 = text[1]
        self.char2 = text[2]
        self.char3 = text[3]
        self.colon = colon
        self.led0 = leds[0]
        self.led1 = leds[1]
        self.led2 = leds[2]
        self.led3 = leds[3]
        
