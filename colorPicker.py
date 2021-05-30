import cv2
import numpy as np
from stackimages import stackImages

def empty(a):
        pass


def colorPicker(image,Scalling_Ratio):

    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars",640,240)
    cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
    cv2.createTrackbar("Hue Max","TrackBars",0,179,empty)
    cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
    cv2.createTrackbar("Sat Max","TrackBars",0,255,empty)
    cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
    cv2.createTrackbar("Val Max","TrackBars",0,255,empty)
    print('press esc to exit')
    while True:
            
            imgHSV=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
            h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
            h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
            s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
            s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
            v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
            v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
            #print(h_min,h_max,s_min,s_max,v_min,v_max)

            lower = np.array([h_min,s_min,v_min])
            upper = np.array([h_max,s_max,v_max])
            mask=cv2.inRange(imgHSV,lower,upper)
            imgResult=cv2.bitwise_and(image,image,mask=mask)
            imgStack = stackImages(Scalling_Ratio,([image,imgResult],[imgHSV,mask]))
            cv2.imshow("Stacked Images- From top left clockwise 1. original 2. Result 3.Mask 4.HSV",imgStack)
            
            if cv2.waitKey(1) & 0xFF == 27:
                break
