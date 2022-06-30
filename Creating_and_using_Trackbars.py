import cv2
print(cv2.__version__)
xPos=0
yPos=0
radius=0
thickness=0
def myCallBack1(val):
    global xPos
    print('xPos', val)
    xPos=val
def myCallBack2(val):
    global yPos
    print('yPos', val)
    yPos=val 
def myCallBack3(val):
    global radius
    print('Radius', val)
    radius=val  
def myCallBack4(val):
    global thickness
    print('Thickness', val)
    thickness=val          
width=640
height=360
cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('my trackBars')
#cv2.resizeWindow('my trackBars',windowWidth,windowHeight)
cv2.resizeWindow('my trackBars',400,200)
cv2.moveWindow('my trackBars',650,0)
cv2.createTrackbar('xPos','my trackBars',0,640,myCallBack1)
cv2.createTrackbar('yPos','my trackBars',0,360,myCallBack2)
cv2.createTrackbar('Radius','my trackBars',0,150,myCallBack3)
cv2.createTrackbar('Thickness','my trackBars',1,10,myCallBack4)
while True:
    ignore, frame=cam.read()
    if thickness==0:
        thickness=(-1)
    cv2.circle(frame,(xPos,yPos),radius,(255,0,0),thickness)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()    
cv2.destroyAllWindows()