from picamera2 import Picamera2

picam2 = None  # Global camera instance

def get_camera():
    global picam2
    if picam2 is None:
        picam2 = Picamera2()
    else:
        picam2.stop()
        picam2 = Picamera2()  # Reinitialize the camera instance
    return picam2

def release_camera():
    global picam2
    if picam2:
        picam2.stop()
        picam2 = None