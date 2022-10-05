import mediapipe as mp
import sys
import struct
import cv2
import time

if len(sys.argv) < 2:
    print("usage: <python> <pose.py> <video.mp4> [start_at_seconds] [duration_seconds]")
    exit(0)

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(sys.argv[1])
# cap = cv2.VideoCapture(1)
#record whole video
cut_at_frame = 9999999999
video_fps = cap.get(cv2.CAP_PROP_FPS)

if len(sys.argv) >= 3:
    #jump to start sec
    cap.set(cv2.CAP_PROP_POS_MSEC, 1000 * int(sys.argv[2]))
if len(sys.argv) >= 4:
    #set max duration
    cut_at_frame = int(sys.argv[3]) * video_fps

frame_count = 0
animation = []
with mp_pose.Pose(min_detection_confidence=0.5,
                min_tracking_confidence=0.5) as pose:

    start = time.time()
    while frame_count < cut_at_frame and cap.isOpened():
        frame_count = frame_count + 1
        success, image = cap.read()

        results = pose.process(image)
        if results.pose_landmarks:
            frame = []
            for node in results.pose_landmarks.landmark:
                joint = []
                joint.append(node.x)
                joint.append(node.y)
                joint.append(node.z)
                frame.append(joint)
            animation.append(frame)

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        end = time.time()
        total_time = end - start
        start = end
        fps = 1 / total_time
        cv2.putText(image, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)

        cv2.imshow('MediaPipe Pose estimation', image)
        if cv2.waitKey(5) & 0xFF == 27:
          break

cap.release()

#serialize
height, width, c = image.shape
f = open('anim.mocap', 'w+b')
f.write(bytearray(struct.pack("i", int(width))))
f.write(bytearray(struct.pack("i", int(height))))
f.write(bytearray(struct.pack("i", int(video_fps))))
f.write(bytearray(struct.pack("i", int(len(animation)))))
f.write(bytearray(struct.pack("i", int(len(animation[0])))))

for frame in animation:
    for joint in frame:
        for axis in joint:
            f.write(bytearray(struct.pack("f", axis)))
f.close()
