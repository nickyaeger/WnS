from smbus2 import SMBus
import time

# I2C address of the display (default is 0x71)
DISPLAY_I2C_ADDRESS = 0x71

# Initialize the I2C bus
bus = SMBus(1)

def clear_display():
    """Clear the display and reset its state."""
    try:
        bus.write_byte(DISPLAY_I2C_ADDRESS, 0x76)  # Clear display command
        time.sleep(0.1)  # Short delay to allow the display to process
    except Exception as e:
        print(f"An error occurred while clearing the display: {e}")

def rearrange_digits(digits):
    """
    Rearrange the input string to account for the display's consistent shifting behavior.

    Args:
        digits (str): A 4-character string containing digits (0-9).

    Returns:
        str: Rearranged string to display correctly.
    """
    # Rotate the string by 1 position to the right
    return digits[-1] + digits[:-1]

def display_digits(digits):
    """
    Display a 4-character string of digits (0-9) on the 7-segment display.

    Args:
        digits (str): A 4-character string containing digits (0-9).
    """
    if len(digits) != 4 or not digits.isdigit():
        print("Error: Input must be a 4-character string containing only digits (0-9).")
        return

    try:
        # Rearrange the digits to compensate for the display's shifting behavior
        adjusted_digits = rearrange_digits(digits)

        # Convert the digits into their ASCII values
        ascii_digits = [ord(d) for d in adjusted_digits]

        # Send all 4 digits in a single I2C transaction
        bus.write_i2c_block_data(DISPLAY_I2C_ADDRESS, 0, ascii_digits)
        print(f"Displayed: {digits} (adjusted to {adjusted_digits})")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    try:
        clear_display()  # Clear the display first
        display_digits("1234")  # Display "1234" on the 7-segment display
        time.sleep(3)  # Wait 3 seconds

        display_digits("5678")  # Display "5678" on the 7-segment display
        time.sleep(3)  # Wait 3 seconds

        display_digits("0000")  # Display "0000" on the 7-segment display
        time.sleep(3)  # Wait 3 seconds
    finally:
        clear_display()  # Clear the display on exit
        bus.close()  # Always close the I2C bus when done
