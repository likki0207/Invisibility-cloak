#importing the required libraries
import streamlit as st
from PIL import Image
import cv2
import numpy as np

#in this we are replacing the red colored pixels with the background pixels to create the 
#invisible effect in the video. 
#For doing this, we have to store the background image for each frame.
cap=cv2.VideoCapture(-1)
count=0
background=0

# Capturing and storing the static background frame
for i in range(60):
	ret,background=cap.read()

### Read every frame from the webcam, until the camera is open
while(cap.isOpened()):
	ret, img = cap.read()
	if not ret:
		break
	count+=1

	# Converting the color space from BGR to HSV
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	# Generating mask to detect red color
	lower_red = np.array([0,120,70])
	upper_red = np.array([10,255,255])
	mask1 = cv2.inRange(hsv,lower_red,upper_red)

	lower_red = np.array([170,120,70])
	upper_red = np.array([180,255,255])
	mask2 = cv2.inRange(hsv,lower_red,upper_red)

	mask1 = mask1+mask2

	# Refining the mask corresponding to the detected red color
	mask1=cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2)
	mask1=cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations = 1)
	mask2=cv2.bitwise_not(mask1)

	# Generating the final output
	res1=cv2.bitwise_and(background,background,mask=mask1)
	res2=cv2.bitwise_and(img,img,mask=mask2)
	output=cv2.addWeighted(res1,1,res2,1,0)

	cv2.imshow('Wow! This is Magic',output)
	
	k=cv2.waitKey(10)
	if k==27:
		break
