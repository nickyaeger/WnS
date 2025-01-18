from smbus2 import SMBus

# I2C address of the display (default is 0x71)
DISPLAY_I2C_ADDRESS = 0x71

# Initialize the I2C bus
bus = SMBus(1)

def clear_display():
    """Clear the display."""
    try:
        bus.write_byte(DISPLAY_I2C_ADDRESS, 0x76)  # Clear display command
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
        # Convert the digits into their ASCII values
        ascii_digits = [ord(d) for d in digits]

        # Always send a full 4-digit block to overwrite all digits
        while len(ascii_digits) < 4:
            ascii_digits.append(32)  # Pad with spaces (ASCII 32) if needed

        # Send the ASCII values directly to the display
        bus.write_i2c_block_data(DISPLAY_I2C_ADDRESS, 0, ascii_digits)
        print(f"Displayed: {digits}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    try:
        clear_display()  # Clear the display first
        display_digits("1234")  # Display "1234" on the 7-segment display
    finally:
        bus.close()  # Always close the I2C bus when done
