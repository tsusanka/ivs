import cv2
import sys
from pre_processing import *
from speech import *
from shapes import *
from enums import *
from config import *
from nao_controller import *


cam_img = get_image_from_camera(ROBOT_IP, ROBOT_PORT)
cv2.imshow('robot_view', cam_img)
cv2.waitKey(0)
sys.exit(0)