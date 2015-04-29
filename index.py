
import numpy as np
import cv2
import sys
from pre_processing import *
from speech import *
from shapes import *

img = cv2.imread('assets/shapes-byr.png')

colors = [Color.YELLOW] # for testing, later add: Color.BLUE, Color.RED,
for color in colors:
	pre_processed = pre_process(img, color)
	contours = find_contours(pre_processed)
	
	img_copy = img.copy()
	draw_contours(img_copy, contours)
	cv2.imshow(color[2], img_copy)


	squares = find_squares(contours)
	cv2.drawContours( img, squares, -1, (0, 255, 0), 3 )
	cv2.imshow('squares', img)

	# sayISee(Shape.TRIANGLE, color[2], format(len(contours))) # TODO: object recognition


cv2.waitKey(0)
sys.exit(0)
