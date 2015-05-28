import cv2
import sys
from pre_processing import *
from speech import *
from shapes import *
from enums import *
from config import *
from camera_controller import *

def projectMain():
    img = get_image_from_camera(ROBOT_IP, ROBOT_PORT)

    found = False
    colors = [Color.YELLOW, Color.BLUE, Color.RED]
    for color in colors:
        pre_processed = pre_process(img, color)
        # pre_processed = extract_color(img, color)
        contours = find_contours(pre_processed)
    
        img_copy = img.copy()
        draw_contours(img_copy, contours)
    
        shapes = find_shapes(contours)

        for key, shape in shapes.iteritems():
            if not shape:
                continue;
            for contours in shape:
                cv2.drawContours( img, shape, -1, (0, 255, 0), 3 )
            sayISee(key, color[2], format(len(shape))) # TODO: object recognition
            found = True
            
    if not found:
        sayISee(0, 0, 0)
