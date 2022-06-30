#detects front face and side Face of left side using cascade profile face but to detect right side i flipped the image and detected right side face also long with left and front face.
import cv2
print(cv2.__version__)
width=640
height=360
cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
frontFaceCascade=cv2.CascadeClassifier('haar\haarcascade_frontalface_default.xml')
sideFaceCascade=cv2.CascadeClassifier('haar\haarcascade_profileface.xml')
while True:
    ignore,frame=cam.read()
    grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frontFaces=frontFaceCascade.detectMultiScale(grayFrame,1.3,5)
    sideFacesLeft=sideFaceCascade.detectMultiScale(grayFrame,1.3,5)
    grayFrameFlipped=cv2.flip(grayFrame,1)
    sideFacesRight=sideFaceCascade.detectMultiScale(grayFrameFlipped,1.3,5)
    for frontFace in frontFaces:
        x,y,w,h=frontFace
        cv2.rectangle(frame,(x,y),(x+w,y+w),(255,0,0),3)
        cv2.rectangle(grayFrameFlipped,(x,y),(x+w,y+w),(255,0,0),3)
    for sideFaceLeft in sideFacesLeft:
        x,y,w,h=sideFaceLeft
        cv2.rectangle(frame,(x,y),(x+w,y+w),(255,0,0),3)   
    for sideFaceRight in sideFacesRight:
        x,y,w,h=sideFaceRight
        cv2.rectangle(grayFrameFlipped,(x,y),(x+w,y+w),(255,0,0),3) 
    cv2.imshow('Flipped',grayFrameFlipped)
    cv2.moveWindow('Flipped',0,height+30)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()    
cv2.destroyAllWindows()