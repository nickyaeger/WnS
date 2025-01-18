from picamera2 import Picamera2
import os
import subprocess

picam2 = None  # Global camera instance

def get_camera():
    global picam2
    # Release any previous camera instance
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
            picam2.stop()  # Properly stop the camera
            print("Camera stopped.")
        except RuntimeError as e:
            print(f"Error stopping the camera: {e}")
        finally:
            # Ensure no leftover processes are holding the camera
            kill_camera_processes()
            picam2 = None
            print("Camera released.")

def kill_camera_processes():
    """Kill any processes holding /dev/video0."""
    try:
        output = subprocess.check_output(["lsof", "/dev/video0"], text=True)
        for line in output.splitlines()[1:]:
            pid = int(line.split()[1])
            if pid != os.getpid():  # Ensure the current script isn't killed
                print(f"Killing process {pid} holding /dev/video0...")
                os.system(f"sudo kill {pid}")
    except subprocess.CalledProcessError:
        print("No processes are holding /dev/video0.")
    except Exception as e:
        print(f"Error checking or killing processes: {e}")
