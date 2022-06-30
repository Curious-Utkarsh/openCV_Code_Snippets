import cv2
print(cv2.__version__)

width=1280
height=720

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
        handsType=[]
        if results.multi_hand_landmarks != None:
            #print(results.multi_handedness)
            for hand in results.multi_handedness:
                #print(hand)
                #print(hand.classification)
                #print(hand.classification[0])
                #print(hand.classification[0].label)
                handType=hand.classification[0].label
                handsType.append(handType)
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for LandMark in handLandMarks.landmark:
                    myHand.append((int(LandMark.x*width),int(LandMark.y*height)))
                myHands.append(myHand)
        return myHands,handsType

findHands=mpHands(2)

while True:
    ignore,frame=cam.read()
    frame=cv2.flip(frame,1)
    myHands,handsType=findHands.parseLandMarks(frame)
    for oneHand,handType in zip(myHands,handsType):
        for fingerTip in [4,8,12,16,20]:
            cv2.circle(frame,oneHand[fingerTip],25,(255,255,255),3)
        cv2.putText(frame,str(handType),(oneHand[8][0],oneHand[8][1]-50),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),2)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()    

