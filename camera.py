from picamera2 import Picamera2
import os

picam2 = None  # Global camera instance

def get_camera():
    global picam2
    # Ensure any previous camera instance is released
    if picam2 is not None:
        release_camera()

    print("Initializing new camera instance...")
    picam2 = Picamera2()
    return picam2

def release_camera():
    global picam2
    if picam2:
        try:
            print("Stopping camera...")
            picam2.stop()  # Stop the camera
            print("Camera stopped.")
        except RuntimeError as e:
            print(f"Error stopping the camera: {e}")
        finally:
            # Forcefully reset the camera device
            print("Force resetting the camera...")
            os.system("sudo systemctl restart libcamera-daemon")  # Restart the camera daemon
            picam2 = None
            print("Camera released and reset.")
