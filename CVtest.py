#THIS CODE IS NOT MINE, I USED CTRL+C AND CTRL+V A LOT
#THIS WAS TO LEARN AND UNDERSTAND WHY THING DO OR DON'T WORK

#https://developers.google.com/mediapipe/solutions/vision/hand_landmarker/python#video
#https://developers.google.com/mediapipe/solutions/vision/hand_landmarker/index#models




'''
# Importing Libraries 
import cv2 
import mediapipe as mp 

# Used to convert protobuf message to a dictionary. 
from google.protobuf.json_format import MessageToDict 

# Initializing the Model 
mpHands = mp.solutions.hands 
hands = mpHands.Hands(static_image_mode=False,model_complexity=1,min_detection_confidence=0.75,min_tracking_confidence=0.75, max_num_hands=2) 

# Start capturing video from webcam 
cap = cv2.VideoCapture(0) 

while True: 
	# Read video frame by frame 
	success, img = cap.read() 

	# Flip the image(frame) 
	img = cv2.flip(img, 1) 

	# Convert BGR image to RGB image 
	imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

	# Process the RGB image 
	results = hands.process(imgRGB) 

	# If hands are present in image(frame) 
	if results.multi_hand_landmarks: 

		# Both Hands are present in image(frame) 
		if len(results.multi_handedness) == 2: 
				# Display 'Both Hands' on the image 
			cv2.putText(img, 'Both Hands', (250, 50), 
						cv2.FONT_HERSHEY_COMPLEX, 
						0.9, (0, 255, 0), 2) 

		# If any hand present 
		else: 
			for i in results.multi_handedness: 
				
				# Return whether it is Right or Left Hand 
				label = MessageToDict(i)['classification'][0]['label']
				if label == 'Left': 
					
					# Display 'Left Hand' on 
					# left side of window 
					cv2.putText(img, label+' Hand', 
								(20, 50), 
								cv2.FONT_HERSHEY_COMPLEX, 
								0.9, (0, 255, 0), 2) 

				if label == 'Right': 
					
					# Display 'Left Hand' 
					# on left side of window 
					cv2.putText(img, label+' Hand', (460, 50), 
								cv2.FONT_HERSHEY_COMPLEX, 
								0.9, (0, 255, 0), 2) 

	# Display Video and when 'q' 
	# is entered, destroy the window 
	cv2.imshow('Image', img) 
	if cv2.waitKey(1) & 0xff == ord('q'): 
		break

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import cv2 
import time

model_path = '/absolute/path/to/hand_landmarker.task'

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode






# Load the frame rate of the video using OpenCV’s CV_CAP_PROP_FPS
# You’ll need it to calculate the timestamp for each frame.

#img.getfield(cv2.CAP_PROP_FPS)


# Loop through each frame in the video using VideoCapture#read()


# Convert the frame received from OpenCV to a MediaPipe’s Image object.
#mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img)

def print_result(result: HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
	print('hand landmarker result: {}'.format(result))

options = HandLandmarkerOptions(base_options=BaseOptions(model_asset_path='absolute/path/to/hand_landmarker.task'),running_mode=VisionRunningMode.LIVE_STREAM,result_callback=print_result)

with HandLandmarker.create_from_options(options) as landmarker:
	cap = cv2.VideoCapture(0)
    
	while True:
		# Read video frame by frame 
		success, img = cap.read() 
		if not success:
			break

		cv2.imshow("img", img)
		#frame = cap.get(cv2.CAP_PROP_FPS)
		timestamp = int(round(time.time() * 1000))

		frame_np = np.array(img)
		mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_np)
		landmarker.detect_async(mp_image, timestamp)


import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import time
import numpy as np
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2


MARGIN = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54)  # vibrant green

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

RESULT = None


# Create a hand landmarker instance with the live stream mode:
def print_result(result: mp.tasks.vision.HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    # print(result)
    global RESULT
    RESULT = result


options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='absolute/path/to/hand_landmarker.task'),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)
with HandLandmarker.create_from_options(options) as landmarker:
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_np = np.array(frame)
        timestamp = int(round(time.time() * 1000))
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_np)
        frame = mp_image.numpy_view()
        landmarker.detect_async(mp_image, timestamp)
        if type(RESULT) is not type(None):
            hand_landmarks_list = RESULT.hand_landmarks
            for idx in range(len(hand_landmarks_list)):
                hand_landmarks = hand_landmarks_list[idx]

                # Draw the hand landmarks.
                hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
                
                hand_landmarks_proto.landmark.extend([
                    landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in
                    hand_landmarks
                ])
                
                solutions.drawing_utils.draw_landmarks(
                    frame,
                    hand_landmarks_proto,
                    solutions.hands.HAND_CONNECTIONS,
                    solutions.drawing_styles.get_default_hand_landmarks_style(),
                    solutions.drawing_styles.get_default_hand_connections_style(),True)
                
        else:
            print('else')
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


import mediapipe as mp

BaseOptions = mp.tasks.BaseOptions
FaceDetector = mp.tasks.vision.FaceDetector
FaceDetectorOptions = mp.tasks.vision.FaceDetectorOptions
FaceDetectorResult = mp.tasks.vision.FaceDetectorResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a face detector instance with the live stream mode:
def print_result(result: FaceDetectorResult, output_image: mp.Image, timestamp_ms: int):
    print('face detector result: {}'.format(result))

options = FaceDetectorOptions(
    base_options=BaseOptions(model_asset_path='/path/to/model.task'),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)
with FaceDetector.create_from_options(options) as detector:
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=numpy_frame_from_opencv)
    detector.detect_async(mp_image, frame_timestamp_ms)
'''

#https://www.geeksforgeeks.org/face-and-hand-landmarks-detection-using-python-mediapipe-opencv/

# Import Libraries
import cv2
import time
import mediapipe as mp

# Grabbing the Holistic Model from Mediapipe and
# Initializing the Model
mp_holistic = mp.solutions.holistic
holistic_model = mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
 
# Initializing the drawing utils for drawing the facial landmarks on image
mp_drawing = mp.solutions.drawing_utils
# (0) in VideoCapture is used to connect to your computer's default camera
capture = cv2.VideoCapture(0)

# Initializing current time and precious time for calcu lating the FPS
previousTime = 0
currentTime = 0

while capture.isOpened():
	# capture frame by frame
	ret, frame = capture.read()

	# resizing the frame for better view
	frame = cv2.resize(frame, (800, 600))

	# Converting the from BGR to RGB
	image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# Making predictions using holistic model
	# To improve performance, optionally mark the image as not writeable to
	# pass by reference.
	image.flags.writeable = False
	results = holistic_model.process(image)
	image.flags.writeable = True

	# Converting back the RGB image to BGR
	image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

	# Drawing Right hand Land Marks
	mp_drawing.draw_landmarks(
	image, 
	results.right_hand_landmarks, 
	mp_holistic.HAND_CONNECTIONS
	)

	# Drawing Left hand Land Marks
	mp_drawing.draw_landmarks(
	image, 
	results.left_hand_landmarks, 
	mp_holistic.HAND_CONNECTIONS
	)
	
	# Calculating the FPS
	currentTime = time.time()
	fps = 1 / (currentTime-previousTime)
	previousTime = currentTime
	
	# Displaying FPS on the image
	cv2.putText(image, str(int(fps))+" FPS", (10, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)

	# Display the resulting image
	cv2.imshow("Hand Landmarks", image)

	# Enter key 'q' to break the loop
	if cv2.waitKey(5) & 0xFF == ord('q'):
		break

# When all the process is done
# Release the capture and destroy all windows
capture.release()
cv2.destroyAllWindows()
