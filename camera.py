import os
import subprocess
from picamera2 import Picamera2

picam2 = None  # Global camera instance

def get_camera():
    global picam2
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
            picam2.stop()
            print("Camera stopped.")
        except RuntimeError as e:
            print(f"Error stopping the camera: {e}")
        finally:
            # Ensure no leftover processes are holding the camera
            kill_camera_process_by_node("/dev/video0")
            picam2 = None
            print("Camera released.")

def kill_camera_process_by_node(device):
    """Kill the process holding a specific device based on its NODE value."""
    try:
        output = subprocess.check_output(["lsof", device], text=True)
        lines = output.splitlines()
        for line in lines[1:]:  # Skip the header line
            parts = line.split()
            pid = int(parts[1])  # PID is the second column
            node = parts[-1]     # NODE is the last column
            print(f"Found process {pid} holding {device} (NODE: {node})")

            # Ensure we don't kill the current script
            if pid != os.getpid():
                print(f"Killing process {pid} holding {device}...")
                os.system(f"sudo kill {pid}")
    except subprocess.CalledProcessError:
        print(f"No processes are holding {device}.")
    except Exception as e:
        print(f"Error checking or killing processes: {e}")
