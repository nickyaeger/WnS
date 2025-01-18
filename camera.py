from picamera2 import Picamera2

picam2 = None  # Global camera instance

def get_camera():
    global picam2
    if picam2 is not None:
        print("Releasing existing camera instance...")
        release_camera()
    print("Initializing new camera instance...")
    picam2 = Picamera2()
    return picam2


def release_camera():
    global picam2
    if picam2:
        try:
            print("Stopping camera...")
            picam2.stop()  # Attempt to stop the camera
            print("Camera stopped.")
        except RuntimeError as e:
            print(f"Error stopping the camera: {e}")
        picam2 = None  # Reset the global instance
        print("Camera released.")
