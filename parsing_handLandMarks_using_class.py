import cv2
print(cv2.__version__)

width=640
height=360

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=.5,tol2=.5):
        self.handsDetect=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
    def parseLandMarks(self,frame):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.handsDetect.process(frameRGB)
        myHands=[]
        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for LandMark in handLandMarks.landmark:
                    myHand.append((int(LandMark.x*width),int(LandMark.y*height)))
                myHands.append(myHand)
        return myHands

findHands=mpHands(2)

while True:
    ignore,frame=cam.read()
    myHands=findHands.parseLandMarks(frame)
    for oneHand in myHands:
        for fingerTip in [4,8,12,16,20]:
            cv2.circle(frame,oneHand[fingerTip],25,(255,255,255),3)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()    

