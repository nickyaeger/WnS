from picamera2 import Picamera2

class CameraManager:
    _instance = None

    @staticmethod
    def get_camera():
        """Get the shared camera instance."""
        if CameraManager._instance is None:
            print("Initializing the camera...")
            CameraManager._instance = Picamera2()
            config = CameraManager._instance.create_preview_configuration(main={"size": (854, 480)})
            CameraManager._instance.configure(config)
            CameraManager._instance.start()
        return CameraManager._instance

    @staticmethod
    def release_camera():
        """Release the shared camera instance."""
        if CameraManager._instance:
            print("Releasing the camera...")
            CameraManager._instance.stop()
            CameraManager._instance = None
            print("Camera released.")
