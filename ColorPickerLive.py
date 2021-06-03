import cv2
import numpy as np
from stackimages import stackImages

frameWidth = 1280
frameHeight = 720
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

 
def empty(a):
    pass
 
cv2.namedWindow("HSV Trackbar")
cv2.resizeWindow("HSV Trackbar", 640, 240)
cv2.createTrackbar("HUE Min", "HSV Trackbar", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV Trackbar", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV Trackbar", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV Trackbar", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV Trackbar", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV Trackbar", 255, 255, empty)
print('press esc to exit')
 
while True:
 
    success, img = cap.read()
    img=np.flip(img,1)
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 
    h_min = cv2.getTrackbarPos("HUE Min", "HSV Trackbar")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV Trackbar")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV Trackbar")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV Trackbar")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV Trackbar")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV Trackbar")
    
 
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
 
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    imgStack=stackImages(0.5,([result,mask],[img,np.zeros_like(img)]))
    #imgStack = np.imgstack([img, mask, result])
    cv2.imshow('Clockwise from top-left: 1. Result 2.Mask 3.Blank Image 4. Original Video', imgStack)
    if cv2.waitKey(1) == 27:
                break
 
cap.release()
cv2.destroyAllWindows()