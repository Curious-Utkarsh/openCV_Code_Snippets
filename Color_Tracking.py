import cv2
import numpy as np
print(cv2.__version__)
def myCallBack1(value):
    global hueLow
    hueLow=value
    print('Hue Low',hueLow)
def myCallBack2(value):
    global hueHigh
    hueHigh=value
    print('Hue High',hueHigh)
def myCallBack3(value):
    global satLow
    satLow=value
    print('Sat Low',satLow)   
def myCallBack4(value):
    global satHigh
    satHigh=value
    print('Sat High',satHigh)
def myCallBack5(value):
    global valLow
    valLow=value
    print('Val Low',valLow)
def myCallBack6(value):
    global valHigh
    valHigh=value
    print('Val High',valHigh)           
width=640
height=360
cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
hueLow=15
hueHigh=24
satLow=10
satHigh=250
valLow=10
valHigh=250
cv2.namedWindow('my Tracker')
cv2.resizeWindow('my Tracker',400,300)
cv2.moveWindow('my Tracker',width,0)
cv2.createTrackbar('Hue Low','my Tracker',15,179,myCallBack1)
cv2.createTrackbar('Hue High','my Tracker',24,179,myCallBack2)
cv2.createTrackbar('Sat Low','my Tracker',10,255,myCallBack3)
cv2.createTrackbar('Sat High','my Tracker',250,255,myCallBack4)
cv2.createTrackbar('Val Low','my Tracker',10,255,myCallBack5)
cv2.createTrackbar('Val High','my Tracker',250,255,myCallBack6)
while True:
    ignore, frame=cam.read()
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerBound=np.array([hueLow,satLow,valLow])
    upperBound=np.array([hueHigh,satHigh,valHigh])
    myMask=cv2.inRange(frameHSV,lowerBound,upperBound)
    myMaskSmall=cv2.resize(myMask,(int(width/2),int(height/2)))
    #myMaskSmall=cv2.bitwise_not(myMaskSmall)
    myObject=cv2.bitwise_and(frame,frame,mask=myMask)
    myObjectSmall=cv2.resize(myObject,(int(width/2),int(height/2)))
    cv2.imshow('My Object',myObjectSmall)
    cv2.moveWindow('My Object',(int(width/2)),height)
    cv2.imshow('My Mask',myMaskSmall)
    cv2.moveWindow('My Mask',0,height)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()    
cv2.destroyAllWindows()
