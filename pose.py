"Pose detection using OpenCV and MediaPipe Pose"

from picamera2 import Picamera2
import cv2
import mediapipe as mp

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Initialize the Pi Camera
picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"size": (854, 480)})
picam2.configure(config)
picam2.start()

while True:
    # Capture a frame
    frame = picam2.capture_array()

    # Rotate the frame 90 degrees clockwise
    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Convert the frame to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_frame)

    # Convert back to BGR for OpenCV display
    frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)

    # Debug: Print frame shape
    print(f"Frame shape: {frame.shape}")

    # Draw landmarks if detected
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Display the rotated frame
    cv2.imshow("Pose Detection", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Stop the camera and clean up
picam2.stop()
cv2.destroyAllWindows()