from smbus2 import SMBus
import time

# I2C address of the display (default is 0x71)
DISPLAY_I2C_ADDRESS = 0x71

# Initialize the I2C bus
bus = SMBus(1)

def clear_display():
    """Clear the display and reset its state."""
    try:
        # Send the "clear display" command
        bus.write_byte(DISPLAY_I2C_ADDRESS, 0x76)
        # Short delay to allow the display to process the clear command
        time.sleep(0.1)
    except Exception as e:
        print(f"An error occurred while clearing the display: {e}")

def display_digits(digits):
    """
    Display a 4-character string of digits (0-9) on the 7-segment display.

    Args:
        digits (str): A 4-character string containing digits (0-9).
    """
    corrected_digits = ""
    corrected_digits += digits[1:5]
    corrected_digits += digits[0]
    if len(corrected_digits) != 4 or not corrected_digits.isdigit():
        print("Error: Input must be a 4-character string containing only digits (0-9).")
        return

    try:
        # Convert the digits into their ASCII values
        ascii_digits = [ord(d) for d in corrected_digits]
        # Send all 4 digits in a single I2C transaction
        bus.write_i2c_block_data(DISPLAY_I2C_ADDRESS, 0, ascii_digits)

        print(f"Displayed: {corrected_digits}")
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

