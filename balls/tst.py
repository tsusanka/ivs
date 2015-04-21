import numpy as np
import cv2
import sys


# TA MRDKA JE V BGR (a nebo je to HSV. Cert vi).Ale tohle na modrou funguje
lower_blue = np.array([100, 100, 100])
upper_blue = np.array([120, 255, 255])

img = cv2.imread('blue_balls_hand2.jpg')
img = cv2.medianBlur(img,5)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsv)


ranged_img = cv2.inRange(hsv, lower_blue, upper_blue)
res = cv2.bitwise_and(img, img, mask=ranged_img)


erode = cv2.erode(ranged_img, None, iterations = 3)
dilate = cv2.dilate(erode, None, iterations = 10)


# HougsCircles don't like to work with filled cicles. Canny does the job.
canny = cv2.Canny(dilate, 200, 300)
circles = cv2.HoughCircles(canny,cv2.cv.CV_HOUGH_GRADIENT,1,50,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

print(circles)
if (circles is not None):
	circles = np.uint16(np.around(circles))
	print(circles)

	for i in circles[0,:]:
	    # draw the outer circle
	    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
	    # draw the center of the circle
	    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

#cv2.imshow('hsv', hsv)
cv2.imshow('ranged', ranged_img)
cv2.imshow('erode', erode)
cv2.imshow('dilate', dilate)
cv2.imshow('canny', canny)
cv2.imshow('img', img)
cv2.waitKey(0)
sys.exit(0)
