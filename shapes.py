
import numpy as np
import cv2
from pre_processing import *

def angle_cos(p0, p1, p2):
	d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
	return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

def find_squares(contours):
	squares = triangles = []
	for contour in contours:
		approx = cv2.approxPolyDP(contour, cv2.arcLength(contour, True)*0.02, True);
		if len(approx) == 4 and cv2.contourArea(approx) > 1000 and cv2.isContourConvex(approx):
			
			# some magic to detect if the angles are ~90 degrees
			approx = approx.reshape(-1,2)
			maxCosine = np.max([angle_cos( approx[i], approx[(i+1) % 4], approx[(i+2) % 4] ) for i in xrange(4)])
			
			if maxCosine < 0.3:
				squares.append(approx)
	return squares
