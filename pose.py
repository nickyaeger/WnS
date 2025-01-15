"Jumping jack pose detection using OpenCV and MediaPipe Pose"

from picamera2 import Picamera2 #type: ignore
import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Initialize the Pi Camera
picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"size": (854, 480)})
picam2.configure(config)
picam2.start()

# Initialize variables for jumping jack detection
jumping_jack_count = 0
prev_state = None  # To track "up" or "down" state

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

    # Detect jumping jacks if landmarks are found
    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark

        # Get relevant landmark positions
        left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST]
        right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST]
        left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        left_ankle = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE]
        right_ankle = landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE]

        # Hands up condition
        hands_up = (
            left_wrist.y < left_shoulder.y and
            right_wrist.y < right_shoulder.y
        )

        # Legs apart condition
        legs_apart = abs(left_ankle.x - right_ankle.x) > 0.3  # Adjust threshold as needed

        # Detect current state ("up" = hands up and legs apart)
        current_state = hands_up and legs_apart

        # Check for state transition to count jumping jacks
        if prev_state is not None and prev_state != current_state:
            if current_state:  # Transition from "down" to "up"
                jumping_jack_count += 1
                print(f"Jumping Jacks: {jumping_jack_count}")

        prev_state = current_state

        # Draw landmarks and connections
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Display the frame with jumping jack count
    cv2.putText(frame, f"Jumping Jacks: {jumping_jack_count}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow("Jumping Jack Detection", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Stop the camera and clean up
picam2.stop()
cv2.destroyAllWindows()
