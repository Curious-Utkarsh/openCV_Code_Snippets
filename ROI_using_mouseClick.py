import cv2
print(cv2.__version__)
evt=0
pnt1=(0,0)
pnt2=(0,0)
def mouseClick(event,xPos,yPos,flag,params):
    global evt
    global pnt
    if event==cv2.EVENT_LBUTTONDOWN:
        print('Event Occured is : ', event)
        print(' at position ', xPos,yPos)
        evt=event
        pnt=(xPos,yPos)
    if event==cv2.EVENT_LBUTTONUP:
        print('Event Occured is : ', event)
        print(' at position ', xPos,yPos)
        evt=event
        pnt=(xPos,yPos)
    if event==cv2.EVENT_RBUTTONUP:
        print('Event Occured is : ', event)
        print(' at position ', xPos,yPos)
        evt=event   
width=640
height=360
cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam', mouseClick)
while True:
    ignore, frame=cam.read()
    if evt==1:
        pnt1=pnt
    if evt==4:
        pnt2=pnt
        #frameROI=frame[yTopLeft:yBottomRight,xTopLeft:xBottomRight]
        cv2.rectangle(frame,pnt1,pnt2,(0,0,255),4)
        frameROI=frame[pnt1[1]:pnt2[1],pnt1[0]:pnt2[0]]
        cv2.imshow('my ROI',frameROI)
        cv2.moveWindow('my ROI',650,0)
    if evt==5:
        evt=0
        cv2.destroyWindow('my ROI')    
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()    
cv2.destroyAllWindows()