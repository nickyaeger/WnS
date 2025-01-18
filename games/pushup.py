"Pushup pose detection using OpenCV and MediaPipe Pose"

from camera import CameraManager
import cv2
import mediapipe as mp
import numpy as np
import sounds
from display_7_seg import display_digits

def start_game():
    print("Starting Jumping Jack Game...")
    sounds.playJacks()

    picam2 = CameraManager.get_camera()

    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    mp_drawing = mp.solutions.drawing_utils

    pushup_count = 0
    direction = 0
    feedback = "Fix Form"

    try:
        while True:
            # Break the loop on 'q' key press or 10 pushups
            if cv2.waitKey(1) & 0xFF == ord('q') or pushup_count >= 10:
                print("Stopping Pushup Game...")
                break

            frame = picam2.capture_array()

            # Convert the frame to RGB for MediaPipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(rgb_frame)

            # Convert back to BGR for OpenCV display
            frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)

            if results.pose_landmarks:
                landmarks = results.pose_landmarks.landmark

                # Get relevant landmark positions
                elbow_angle = calculate_angle(landmarks, mp_pose.PoseLandmark.LEFT_SHOULDER, mp_pose.PoseLandmark.LEFT_ELBOW, mp_pose.PoseLandmark.LEFT_WRIST)
                shoulder_angle = calculate_angle(landmarks, mp_pose.PoseLandmark.LEFT_ELBOW, mp_pose.PoseLandmark.LEFT_SHOULDER, mp_pose.PoseLandmark.LEFT_HIP)
                hip_angle = calculate_angle(landmarks, mp_pose.PoseLandmark.LEFT_SHOULDER, mp_pose.PoseLandmark.LEFT_HIP, mp_pose.PoseLandmark.LEFT_KNEE)

                # Percentage of success for the pushup
                per = np.interp(elbow_angle, (90, 160), (0, 100))

                # Bar to show pushup progress
                bar = np.interp(elbow_angle, (90, 160), (380, 50))

                # Check to ensure the correct form before starting
                if elbow_angle > 160 and shoulder_angle > 40 and hip_angle > 160:
                    feedback = "Good Form"
                else:
                    feedback = "Fix Form"

                # Check for full range of motion for the pushup
                if feedback == "Good Form":
                    if per == 0:
                        if elbow_angle <= 90 and hip_angle > 160:
                            feedback = "Up"
                            if direction == 0:
                                pushup_count += 0.5
                                direction = 1
                        else:
                            feedback = "Fix Form"

                    if per == 100:
                        if elbow_angle > 160 and shoulder_angle > 40 and hip_angle > 160:
                            feedback = "Down"
                            if direction == 1:
                                pushup_count += 0.5
                                direction = 0
                        else:
                            feedback = "Fix Form"

                # Draw Bar
                cv2.rectangle(frame, (580, 50), (600, 380), (0, 255, 0), 3)
                cv2.rectangle(frame, (580, int(bar)), (600, 380), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, f'{int(per)}%', (565, 430), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

                # Pushup Counter
                cv2.rectangle(frame, (0, 380), (100, 480), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, str(int(pushup_count)), (25, 455), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

                # Feedback
                cv2.rectangle(frame, (500, 0), (640, 40), (255, 255, 255), cv2.FILLED)
                cv2.putText(frame, feedback, (500, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

                # Draw landmarks and connections
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            cv2.imshow("Push-up Detection", frame)

    finally:
        cv2.destroyAllWindows()
    return

def calculate_angle(landmarks, p1, p2, p3):
    x1, y1 = landmarks[p1].x, landmarks[p1].y
    x2, y2 = landmarks[p2].x, landmarks[p2].y
    x3, y3 = landmarks[p3].x, landmarks[p3].y

    angle = np.degrees(np.arctan2(y3 - y2, x3 - x2) - np.arctan2(y1 - y2, x1 - x2))
    if angle < 0:
        angle += 360
    if angle > 180:
        angle = 360 - angle

    return angle
