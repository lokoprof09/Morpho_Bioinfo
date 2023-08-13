import cv2
import dlib
import glob
import numpy as np
import pandas as pd


# set up the 68 point facial landmark detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
filename = "New-DS/big-neutra.jpg" #sample image file or folder
img = cv2.imread(filename, 1)

# midpoint function
def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

# convert to grayscale, but we dont need to
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# detect faces in the image
faces_in_image = detector(img_gray, 1)

# loop through each face in image and print rectangle
for face in faces_in_image:
	x, y = face.left(), face.top()
	x1, y1 = face.right(), face.bottom()
	cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
    
#generating custom anatomical landmarks
	landmarks = predictor(img_gray, face)

# extracts custom anatomical points using midpoint function
m_eye_top = midpoint(landmarks.part(21), landmarks.part(22))

l_eye_top = midpoint(landmarks.part(37), landmarks.part(38))
l_eye_bottom = midpoint(landmarks.part(41), landmarks.part(40))

r_eye_top = midpoint(landmarks.part(43), landmarks.part(44))
r_eye_bottom = midpoint(landmarks.part(47), landmarks.part(46))

m_chin = midpoint(landmarks.part(57), landmarks.part(8))

#place points on coordinate location

l_eye_top_pt = cv2.circle(img, l_eye_top, 3, (0, 0, 255), -1)
l_eye_bottom_pt = cv2.circle(img, l_eye_bottom, 3, (0, 0, 255), -1)

r_eye_top_pt = cv2.circle(img, r_eye_top, 3, (0, 0, 255), -1)
r_eye_bottom_pt = cv2.circle(img, r_eye_bottom, 3, (0, 0, 255), -1)
m_eye_top_pt = cv2.circle(img, m_eye_top, 3, (0, 0, 255), -1)
m_chin_pt = cv2.circle(img, m_chin, 3, (0, 0, 255), -1)

print("LM=38")
#array of default anatomical landmarks
a = [36, 39, 42, 45, 27, 30, 31, 32, 33, 34, 35, 48, 54, 50, 51, 52, 57, 62, 66, 8, 6, 10, 4, 12, 1, 15, 17, 19, 21, 22, 24, 26]

for n1 in a:
    xa = landmarks.part(n1).x
    ya = landmarks.part(n1).y
    cv2.circle(img, (xa, ya), 3, (0, 0, 255), -1)
    print(xa, ya)

print(m_eye_top)
print(m_chin)
print(l_eye_top)
print(r_eye_top)
print(l_eye_bottom)
print(r_eye_bottom)
print("ID=1")

# show the output image with the face detections + facial landmarks in red
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()