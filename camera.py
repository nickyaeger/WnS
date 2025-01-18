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
    """Release the camera properly and kill any stuck processes."""
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

            pid = int(parts[1])  # PID is always the second column
            node = parts[-2]     # NODE is the second-to-last column
            device_path = parts[-4]  # Device path is the 4th-to-last column

            # Log the process holding the device
            print(f"Found process {pid} holding {device} (NODE: {node})")

            # Stop the current process if it's holding the camera
            if pid == os.getpid():
                print(f"Releasing current script's process (PID: {pid}) holding {device}...")
                if picam2:
                    picam2.stop()
                    print("Camera released by the current script.")
            else:
                # Kill other processes holding the camera
                print(f"Killing process {pid} holding {device} (NODE: {node})...")
                os.system(f"sudo kill {pid}")
                print(f"Process {pid} terminated.")
    except subprocess.CalledProcessError:
        print(f"No processes are holding {device}.")
    except Exception as e:
        print(f"Error checking or killing processes: {e}")


