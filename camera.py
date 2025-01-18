from picamera2 import Picamera2

class CameraManager:
    _instance = None

    @staticmethod
    def get_camera():
        """Get the shared camera instance."""
        if CameraManager._instance is None:
            try:
                print("Initializing the camera...")
                CameraManager._instance = Picamera2()
                config = CameraManager._instance.create_preview_configuration(main={"size": (854, 480)})
                CameraManager._instance.configure(config)
                CameraManager._instance.start()
                print("Camera initialized and running.")
            except RuntimeError as e:
                print(f"Failed to initialize camera: {e}")
                print("Attempting to recover...")
                CameraManager.release_camera()  # Force cleanup
                return CameraManager.get_camera()  # Retry initialization
        return CameraManager._instance

    @staticmethod
    def release_camera():
        """Release the shared camera instance."""
        if CameraManager._instance:
            try:
                print("Stopping the camera...")
                CameraManager._instance.stop()
                print("Camera stopped.")
            except RuntimeError as e:
                print(f"Error stopping the camera: {e}")
            finally:
                CameraManager._instance = None
                print("Camera released.")
