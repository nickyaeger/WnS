"Pushup pose detection using OpenCV and MediaPipe Pose"

from picamera2 import Picamera2
import cv2
import mediapipe as mp

def start_game():
    print("Starting Pushup Game...")
    picam2 = Picamera2()
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    mp_drawing = mp.solutions.drawing_utils

    config = picam2.create_preview_configuration(main={"size": (854, 480)})
    picam2.configure(config)
    picam2.start()
    
    pushup_count = 0
    prev_state = None  # To track "up" or "down" state
    
    while True:
        # Break the loop on 'q' key press or 10 pushups
        if cv2.waitKey(1) & 0xFF == ord('q') or pushup_count >= 5:
            print("Stopping Pushup Game...")
            picam2.stop()
            cv2.destroyAllWindows()
            exit()

        frame = picam2.capture_array()
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    
        # Convert the frame to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb_frame)
    
        # Convert back to BGR for OpenCV display
        frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)
    
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            # Get relevant landmark positions
            nose_y = landmarks[mp_pose.PoseLandmark.NOSE].y
            shoulders_y = (landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].y +
                           landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].y) / 2
            # Push-up "down" condition: nose close to shoulder level
            is_down = nose_y > shoulders_y + 0.05  # Adjust threshold as needed
            # Push-up "up" condition: nose far above shoulder level
            is_up = nose_y < shoulders_y - 0.05  # Adjust threshold as needed
            # State transition for counting push-ups
            if prev_state is not None and prev_state != (is_up, is_down):
                if is_down and not is_up:  # Transition to "down"
                    prev_state = (is_up, is_down)
                elif is_up and not is_down:  # Transition to "up"
                    pushup_count += 1
                    print(f"Push-ups: {pushup_count}")
                    prev_state = (is_up, is_down)
            else:
                prev_state = (is_up, is_down)

            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    
        cv2.putText(frame, f"Push-ups: {pushup_count}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow("Push-up Detection", frame)
    