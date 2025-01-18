from smbus2 import SMBus
import time

# I2C address of the display (default is 0x71, can be changed via jumpers)
DISPLAY_I2C_ADDRESS = 0x71

# Initialize the I2C bus
bus = SMBus(1)  # Use I2C bus 1 (default on most Raspberry Pi models)

def send_command(command):
    """Send a single-byte command to the display."""
    bus.write_byte(DISPLAY_I2C_ADDRESS, command)

def send_data(data):
    """Send a string or data to the display."""
    if isinstance(data, str):
        bus.write_i2c_block_data(DISPLAY_I2C_ADDRESS, 0, list(data.encode()))
    elif isinstance(data, list):
        bus.write_i2c_block_data(DISPLAY_I2C_ADDRESS, 0, data)
    else:
        bus.write_byte(DISPLAY_I2C_ADDRESS, data)

def clear_display():
    """Clear the display."""
    send_command(0x76)  # Clear display command

def set_brightness(brightness):
    """Set the brightness of the display (0-255)."""
    if 0 <= brightness <= 255:
        send_command(0x7A)  # Brightness command
        send_data([brightness])
    else:
        print("Brightness value out of range. Must be between 0 and 255.")

def print_number(number):
    """Display a number on the display."""
    send_data(str(number))  # Send number as a string

def print_message(message):
    """Display a custom message on the display."""
    send_data(message)  # Send custom message

def set_decimal_points(bitmask):
    """
    Set the decimal points on the display.
    Each bit of the bitmask corresponds to a decimal point.
    """
    if 0 <= bitmask <= 0x0F:  # Ensure bitmask is within valid range
        send_command(0x77)  # Set decimal points command
        send_data([bitmask])
    else:
        print("Bitmask value out of range. Must be between 0 and 15.")

def test_display():
    """
    Run a test sequence to demonstrate the display's functionality.
    """
    try:
        print("Starting I2C test...")
        clear_display()
        time.sleep(1)

        print("Setting brightness to 50%...")
        set_brightness(128)
        time.sleep(1)

        print("Displaying number 1234...")
        print_number(1234)
        time.sleep(2)

        print("Enabling decimal points...")
        set_decimal_points(0b1010)  # Enable decimal points on digits 1 and 3
        time.sleep(2)

        print("Displaying message 'HiPi'...")
        print_message("HiPi")
        time.sleep(2)

        print("Clearing display...")
        clear_display()
        print("Test complete.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        clear_display()
        bus.close()

# Main script entry point
if __name__ == "__main__":
    test_display()
