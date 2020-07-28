# Invisibility-cloak
-> This code helps you to understand the invisibilty cloak which basically uses color segmentation 
   and a bit of image processing to replace the foreground object of interest with the background.
   
-> You just need to take a unicolor cloth and apply color segmentation on it. 

-> After that take a picture of the background and place the cloth on yourself to virtually disappear.

# Code Requirements :
(a) opencv
(b) numpy

# Installing the required packages:
To install the opencv package use the following command:

-> pip install opencv-python

To install the numpy package use the following command:

-> pip install numpy

# Steps to Build this project:
(1) At first we will be importing the required packages

(2) Open the inbuilt Camera

(3) Now we will capture the frames from the camera

(4) Get the HSV image

(5) Create a mask with the segmented HSV color

(6)  Using bitwise add, create the mask for background and foreground

(7) Add background and foreground and create the final frame 

(8) Finally display the final frame


# Working Example:
![](working_video.gif)


# Execution:
To run the code, type the following command:

-> python invisible1.py


