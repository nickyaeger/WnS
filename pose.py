"Pose detection using OpenCV and MediaPipe Pose"

import mediapipe as mp
import cv2 as cv

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera. Exiting...")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame. Exiting...")
        break

    image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    result = pose.process(image)
    if result.pose_landmarks:
        mp_drawing.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv.imshow('Pose Detection', frame)

    if cv.waitKey(10) == ord('q'):
        break
    
cv.destroyAllWindows()
pose.close()
cap.release()