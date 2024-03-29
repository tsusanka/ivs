import numpy as np
import cv2
import sys

def find_contours(image):
    (contours, _) = cv2.findContours(image,
                                    cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)
    return contours

def draw_contours(image, contours):
    for c in contours:
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)


def find_hough_circles(image):
    # HougsCircles don't like working with filled cicles. Canny does the job.
    canny = cv2.Canny(image, 200, 300)
    circles = cv2.HoughCircles(canny,cv2.cv.CV_HOUGH_GRADIENT,1,50,
                                param1=50,param2=30,minRadius=0,maxRadius=0)
    return circles


def draw_hough_circles(image, circles):
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(image,(i[0],i[1]),2,(0,0,255),3)

def pre_process(image, color):
    ranged_img = extract_color(image, color)
    erode = cv2.erode(ranged_img, None, iterations = 3)
    dilate = cv2.dilate(erode, None, iterations = 10)
    return dilate

def extract_color(image, color):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    ranged_img = cv2.inRange(hsv, color[0], color[1])
    if color[2] == 'red':
        second_range = cv2.inRange(hsv, color[3], color[4])
        cv2.add(ranged_img, second_range, ranged_img)
    return ranged_img
