import cv2
import time
print(cv2.__version__)
width = 640
height = 320
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
tLast=time.time()
time.sleep(0.1)
while True:
    dT=time.time()-tLast
    fps=int(1/dT)
    print(fps)
    tLast=time.time()
    ignore, frame=cam.read()
    cv2.putText(frame, (str(fps)+' FPS'), (40,80), cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255),1)
    cv2.imshow('My webCam', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()


