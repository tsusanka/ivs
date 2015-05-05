import cv2
import sys
from config import *
from nao_controller import *


cam_img = get_image_from_camera(ROBOT_IP, ROBOT_PORT)
print("Retrieved CV2 image:")
print("\trows,cols,channels: ", cam_img.shape)
print("\t# pixels= ", cam_img.size)
print("\ttype: ", cam_img.dtype)

cv2.imshow('robot_view', cam_img)
cv2.waitKey(0)
sys.exit(0)