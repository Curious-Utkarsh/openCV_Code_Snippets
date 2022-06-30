import cv2
print(cv2.__version__)
import mediapipe as mp

width = 640
height = 360

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

handsDetect=mp.solutions.hands.Hands(False,2,.5,.5)
mpDraw=mp.solutions.drawing_utils

def parseLandMarks(frame):

    myHands=[]
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=handsDetect.process(frameRGB)
    if results.multi_hand_landmarks != None:
        for handLandMarks in results.multi_hand_landmarks:
            myHand=[]
            for LandMark in handLandMarks.landmark:
                myHand.append((int(LandMark.x*width),int(LandMark.y*height)))
            myHands.append(myHand)
    return myHands

while True:
    ignore,frame=cam.read()
    MYHands=parseLandMarks(frame)
    for oneHand in MYHands:
        for fingerTip in [8,12,16,20]:
            cv2.circle(frame,oneHand[fingerTip],15,(255,255,255),2)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()




