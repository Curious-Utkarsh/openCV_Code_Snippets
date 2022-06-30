import cv2
print(cv2.__version__)
width=640
height=360
cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
faceCascade=cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')
eyeCascade=cv2.CascadeClassifier('haar/haarcascade_eye.xml')
while True:
    ignore,frame=cam.read()
    grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(grayFrame,1.3,5)
    for face in faces:
        x,y,W,H=face
        cv2.rectangle(frame,(x,y),(x+W,y+H),(0,0,255),3)
        frameROI=frame[y:y+H,x:x+W] #frameROI=frame[rowsStart:rowsEnd,columnStart:columnEnd
        frameROIGray=cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
        eyes=eyeCascade.detectMultiScale(frameROIGray)
        for eye in eyes:
            Xeye,Yeye,Weye,Heye=eye
            cv2.rectangle(frameROI,(Xeye,Yeye),(Xeye+Weye,Yeye+Heye),(255,0,0),2)       
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()    
cv2.destroyAllWindows()