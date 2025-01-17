from picamera2 import Picamera2
import cv2
import mediapipe as mp

picam2 = Picamera2()
game_active = False

def start_game():
    print("Starting Pushup Game...")
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    mp_drawing = mp.solutions.drawing_utils
    
    picam2 = Picamera2()
    config = picam2.create_preview_configuration(main={"size": (854, 480)})
    picam2.configure(config)
    picam2.start()
    
    pushup_count = 0
    prev_state = None  # To track "up" or "down" state
    
    while True:
        # Break the loop on 'q' key press or 5 pushups
        if cv2.waitKey(1) & 0xFF == ord('q') or pushup_count >= 5:
            stop_game()

        frame = picam2.capture_array()
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    
        # Convert the frame to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb_frame)
    
        # Convert back to BGR for OpenCV display
        frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)
    
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
    
            nose = landmarks[mp_pose.PoseLandmark.NOSE]
            shoulders_y = (landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].y +
                           landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].y) / 2
            hips_y = (landmarks[mp_pose.PoseLandmark.LEFT_HIP].y +
                      landmarks[mp_pose.PoseLandmark.RIGHT_HIP].y) / 2
    
            # Push-up "down" condition: nose is close to shoulders' Y level
            # and hips are significantly higher than shoulders (body alignment)
            is_down = nose.y < shoulders_y and hips_y > shoulders_y + 0.1
    
            # Push-up "up" condition: nose is far above shoulders' Y level
            # and body alignment is maintained
            is_up = nose.y > shoulders_y + 0.2 and hips_y > shoulders_y
    
            # Determine state transition
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

def stop_game():
    print("Stopping Pushup Game...")
    picam2.stop()
    cv2.destroyAllWindows()