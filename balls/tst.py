import numpy as np
import cv2

img = cv2.imread('red_balls.png')
img2 = cv2.medianBlur(img, 5)
ret, th3 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
hsv2 = cv2.cvtColor(th3, cv2.COLOR_RGB2GRAY)

erode = cv2.erode(hsv2, None, iterations = 3)
dilate = cv2.dilate(erode, None, iterations = 10)
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
