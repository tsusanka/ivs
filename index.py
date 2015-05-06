
import cv2
import sys
from pre_processing import *
from speech import *
from shapes import *
from enums import *
from config import *

img = cv2.imread('assets/shapes-byr.png')

colors = [Color.YELLOW, Color.BLUE, Color.RED]
for color in colors:
	pre_processed = extract_color(img, color)
	contours = find_contours(pre_processed)

	img_copy = img.copy()
	draw_contours(img_copy, contours)
	cv2.imshow(color[2], img_copy)

	shapes = find_shapes(contours)

	for key, shape in shapes.iteritems():
		if not shape:
			continue
		for contours in shape:
			cv2.drawContours( img, shape, -1, (0, 255, 0), 3 )
		sayISee(key, color[2], format(len(shape))) # TODO: object recognition
	
	cv2.imshow('shapes', img)


cv2.waitKey(0)
sys.exit(0)
