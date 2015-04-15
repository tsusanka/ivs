import numpy as np
import cv2
import sys

iLowH = 170;
iHighH = 179;

iLowS = 150; 
iHighS = 255;

iLowV = 60;
iHighV = 255;


# TA MRDKA JE V BGR
lower_blue = np.array([95,250,130])
upper_blue = np.array([105,255,255])

img = cv2.imread('balls_susi.jpg')
# ret, th3 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsv)


#ranged_img = cv2.inRange(img, np.array([iLowH, iLowS, iLowV]), np.array([iHighH, iHighS, iHighV]))
ranged_img = cv2.inRange(hsv, lower_blue, upper_blue)

res = cv2.bitwise_and(img,img, mask= ranged_img)



oMoments = cv2.moments(ranged_img);

print oMoments
dM01 = oMoments['m01'];
dM10 = oMoments['m10'];
dArea = oMoments['m00'];

posX = dM10 / dArea;
posY = dM01 / dArea;  

print posX
print posY

cv2.line(ranged_img, (0,0), (int(posX), int(posY)), (255,50,0),5)
cv2.imshow('ranged', ranged_img)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
sys.exit(0)


#erode = cv2.erode(hsv2, None, iterations = 3)
#dilate = cv2.dilate(erode, None, iterations = 10)
contours,hierarchy = cv2.findContours(erode, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

f = cv2.imread('red_balls.png')
for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        cx,cy = x+w/2, y+h/2
        
        if 20 < hsv.item(cy,cx,0) < 30:
            cv2.rectangle(f,(x,y),(x+w,y+h),[0,255,255],2)
            print "yellow :", x,y,w,h
        elif 100 < hsv.item(cy,cx,0) < 120:
            cv2.rectangle(f,(x,y),(x+w,y+h),[255,0,0],2)
            print "blue :", x,y,w,h


#cnt = contours[4]
#img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)
img3 = cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('img', img)
cv2.imshow('hsv', hsv)
cv2.imshow('th3', th3)
cv2.imshow('erode', erode)
cv2.imshow('dilate', dilate)
#cv2.imshow('img3', img3)
cv2.imshow('hsv2', hsv2)
cv2.imshow('f', f)
cv2.waitKey(0)
cv2.destroyAllWindows()
