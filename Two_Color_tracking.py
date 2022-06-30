#For Tracking Two Colors Simultaneously or to track red color better.
import cv2
import numpy as np
print(cv2.__version__)
def myCallBack1(value):
    global hueLow1
    hueLow1=value
    print('Hue Low 1',hueLow1)
def myCallBack2(value):
    global hueHigh1
    hueHigh1=value
    print('Hue High 1',hueHigh1)
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
def myCallBack7(value):
    global hueLow2
    hueLow2=value
    print('Hue Low 2',hueLow2)
def myCallBack8(value):
    global hueHigh2
    hueHigh2=value
    print('Hue High 2',hueHigh2)
width=640
height=360
cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
hueLow1=10
hueHigh1=20
satLow=10
satHigh=250
valLow=10
valHigh=250
hueLow2=10
hueHigh2=20
cv2.namedWindow('my Trackers')
cv2.resizeWindow('my Trackers',400,400)
cv2.moveWindow('my Trackers',width,0)
cv2.createTrackbar('Hue Low 1','my Trackers',10,179,myCallBack1)
cv2.createTrackbar('Hue High 1','my Trackers',20,179,myCallBack2)
cv2.createTrackbar('Hue Low 2','my Trackers',10,179,myCallBack7)
cv2.createTrackbar('Hue High 2','my Trackers',20,179,myCallBack8)
cv2.createTrackbar('Sat Low','my Trackers',10,255,myCallBack3)
cv2.createTrackbar('Sat High','my Trackers',250,255,myCallBack4)
cv2.createTrackbar('Val Low','my Trackers',10,255,myCallBack5)
cv2.createTrackbar('Val High','my Trackers',250,255,myCallBack6)
while True:
    ignore, frame=cam.read()
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerBound1=np.array([hueLow1,satLow,valLow])
    upperBound1=np.array([hueHigh1,satHigh,valHigh])
    lowerBound2=np.array([hueLow2,satLow,valLow])
    upperBound2=np.array([hueHigh2,satHigh,valHigh])
    myMask1=cv2.inRange(frameHSV,lowerBound1,upperBound1)
    myMask2=cv2.inRange(frameHSV,lowerBound2,upperBound2)
    #myMaskComposite= myMask1 | myMask2 #(OR)
    myMaskComposite=cv2.add(myMask1,myMask2)
    myMaskSmall1=cv2.resize(myMask1,(int(width/2),int(height/2)))
    myMaskSmall2=cv2.resize(myMask2,(int(width/2),int(height/2)))
    myMaskCompositeSmall=cv2.resize(myMaskComposite,(int(width/2),int(height/2)))
    myObjects=cv2.bitwise_and(frame,frame,mask=myMaskComposite)
    myObjectsSmall=cv2.resize(myObjects,(int(width/2),int(height/2)))
    cv2.imshow('My Mask 1',myMaskSmall1)
    cv2.moveWindow('My Mask 1',0,height+30)
    cv2.imshow('My Mask 2',myMaskSmall2)
    cv2.moveWindow('My Mask 2',0,(height+int(height/2)+60))
    cv2.imshow('My Mask Composite',myMaskCompositeSmall)
    cv2.moveWindow('My Mask Composite',int(width/2),height+30)
    cv2.imshow('My Objects of Interest',myObjectsSmall)
    cv2.moveWindow('My Objects of Interest',int(width/2),(height+int(height/2)+60))
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()    
cv2.destroyAllWindows()
