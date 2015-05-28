import cv2
import sys
from pre_processing import *
from speech import *
from shapes import *
from enums import *
from config import *
from camera_controller import *

def projectMain():
    img = cv2.imread('assets/resize6.png')

    found = False
    colors = [Color.YELLOW, Color.BLUE, Color.RED]
    for color in colors:
        pre_processed = pre_process(img, color)
        # pre_processed = extract_color(img, color)
        contours = find_contours(pre_processed)
    
        img_copy = img.copy()
        draw_contours(img_copy, contours)
        cv2.imshow(color[2], img_copy)
    
        shapes = find_shapes(contours)

        for key, shape in shapes.iteritems():
            if not shape:
                continue;
            for contours in shape:
                cv2.drawContours( img, shape, -1, (0, 255, 0), 3 )
            printISee(key, color[2], format(len(shape))) # TODO: object recognition
            found = True

    if not found:
        printISee(0, 0, 0)
    
    cv2.waitKey(0)
    sys.exit(0)
