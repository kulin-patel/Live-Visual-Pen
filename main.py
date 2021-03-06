import cv2
import numpy as np
import time

frameWidth = 1280
frameHeight = 720
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
pTime = 0
cTime = 0


myColors = [[0,120,157,20,255,255]] #orange
            
            #[57,76,0,100,255,255],[90,48,0,118,255,255]#purple
PenColors = [[51,153,255]]#orange
                
                #[0,255,0], #green
                #[255,0,0]] 
                #[255,0,255]#Pink
myPoints = []  #x,y,colorID

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>150:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            #Where will be point of your pen?
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True) #approx gives  polygon vertice location
            
            x, y, w, h = cv2.boundingRect(approx) # from x,y we can decide pen tip
    return x+w//2,y

def findColor(img,myColor,PenColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y= getContours(mask)
        cv2.circle(imgResult,(x,y),5,PenColors[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
        #cv2.imshow(str(color[0]),mask)
    return newPoints



def drawOnCanvas(myPoints,PenColors):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, PenColors[point[2]], cv2.FILLED) 

while True:
    success, img = cap.read()
    img= cv2.flip(img,1)
    imgResult= img.copy()
    newPoints = findColor(img, myColors,PenColors) 

    if len(newPoints)!=0:
            for newP in newPoints:
                myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,PenColors)
    
    #Write frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(imgResult, "FPS= " + str(int(fps)), (10, 20), cv2.FONT_HERSHEY_PLAIN, 1,(0, 0, 0), 1)
    
    cv2.imshow("Result", imgResult)
    
    if cv2.waitKey(1) ==27:
        break