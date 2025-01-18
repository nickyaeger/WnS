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
        # corrected_digits = ""
        # corrected_digits += digits[1:5]
        # corrected_digits += digits[0]
        # print(f"Corrected: {corrected_digits}")
        clear_display()  # Clear the display first
        time.sleep(0.03)
        for position, digit in enumerate(digits):
            ascii_value = ord(digit)  # Convert digit to ASCII
            bus.write_i2c_block_data(DISPLAY_I2C_ADDRESS, 0x7B, [position, ascii_value])
            time.sleep(0.1)  # Small delay between digit updates

        print(f"Displayed: {digits}")
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
