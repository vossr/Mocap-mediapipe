import mediapipe as mp
import cv2
from google.protobuf.json_format import MessageToDict

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)

with mp_hands.Hands(max_num_hands=4, min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands: 
	while cap.isOpened():
		ret, frame = cap.read()
		image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		results = hands.process(image)
		image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
		
		if results.multi_hand_landmarks:
			for num, hand in enumerate(results.multi_hand_landmarks):
				#read tracking data from protcol buffers
				handedness = MessageToDict(results.multi_handedness[num])
				handcolor = (0, 0, 255)
				if handedness["classification"][0]["label"] == 'Left':
					handcolor = (255, 0, 0)
				mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
										mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=4),
										mp_drawing.DrawingSpec(handcolor, thickness=2, circle_radius=2))

		cv2.imshow('Hand Tracking', image)
		if cv2.waitKey(5) & 0xFF == 27:
			break

cap.release()
cv2.destroyAllWindows()
