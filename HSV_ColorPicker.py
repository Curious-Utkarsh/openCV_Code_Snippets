import cv2
import numpy as np
print(cv2.__version__)
evt=0
pnt=(0,0)
def mouseClick(event,xPos,yPos,flags,params):
    global evt
    global pnt
    if event==cv2.EVENT_LBUTTONDOWN:
        print('Event Occured is :', event)
        print('At Position',xPos,yPos)
        evt=event
        pnt=(xPos,yPos)
width=640
height=360
cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam',mouseClick)
while True:
    ignore, frame=cam.read()
    if evt==1:
        x=np.zeros([250,250,3],dtype=np.uint8)
        y=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #color=frame[yPos(i,e rows)][xPos(i,e coloumns)]
        color=y[pnt[1]][pnt[0]]
        print(color)
        x[:,:]=color
        cv2.putText(x,(str(color)),(0,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
        cv2.imshow('Color Picker',x)
        cv2.moveWindow('Color Picker',width,0)
        evt=0
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()    
cv2.destroyAllWindows()