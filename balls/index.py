
import numpy as np
import cv2
import sys
from pre_processing import *
from speech import *

img = cv2.imread('color_balls4.jpg')

colors = [Color.BLUE, Color.YELLOW, Color.RED]
for color in colors:
	pre_processed = pre_process(img, color)
	contours = find_contours(pre_processed)
	
	img_copy = img.copy()
	draw_contours(img_copy, contours)
	cv2.imshow(color[2], img_copy)


	sayISee(Shape.TRIANGLE, color[2], format(len(contours))) # TODO: object recognition


cv2.waitKey(0)
sys.exit(0)
