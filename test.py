from cv2.cv import *

img = LoadImage("/mnt/img.jpg")
NamedWindow("opencv")
ShowImage("opencv",img)
WaitKey(0)
