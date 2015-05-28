
import numpy as np
import cv2
import math
from pre_processing import *
from enums import *

def angle_cos(p0, p1, p2):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

def find_shapes(contours):
    shapes = {}
    shapes[Shape.RECTANGLE] = []
    shapes[Shape.TRIANGLE] = []
    shapes[Shape.HEXAGON] = []
    shapes[Shape.PENTAGON] = []
    shapes[Shape.CIRCLE] = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour, cv2.arcLength(contour, True)*0.04, True);
        area = cv2.contourArea(approx)

        # Skip small or non-convex objects
        if area < 100 or not cv2.isContourConvex(approx):
            continue;

        if len(approx) == 3:
            shapes[Shape.TRIANGLE].append(approx)

        elif len(approx) == 4:
            # some magic to detect if the angles are ~90 degrees
            approx = approx.reshape(-1,2)
            maxCosine = np.max([angle_cos( approx[i], approx[(i+1) % 4], approx[(i+2) % 4] ) for i in xrange(4)])

            if maxCosine < 0.3:
                shapes[Shape.RECTANGLE].append(approx)
        
        elif len(approx) == 5:
            shapes[Shape.PENTAGON].append(approx)

        elif len(approx) == 6:
            shapes[Shape.HEXAGON].append(approx)

        elif len(approx) >= 7:
            # x,y, width, height = cv2.boundingRect(contour)
            # radius = width / 2

            # if abs(1 - (width / height)) <= 0.2 and abs(1 - (area / (math.pi * math.pow(radius, 2)))) <= 0.2:
            shapes[Shape.CIRCLE].append(contour)

    return shapes
