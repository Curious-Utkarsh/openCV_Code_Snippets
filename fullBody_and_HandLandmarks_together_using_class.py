import cv2
print(cv2.__version__)
import numpy as np

width=1280
height=720

cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

class mpBody:
    x=np.zeros([height,width,3],dtype=np.uint8)
    x[:,:]=(0,0,0)
    import mediapipe as mp
    def __init__(self,stillImage=False,upperBody=False,smoothData=True,tol1=.5,tol2=.5):
        self.bodyDetect=self.mp.solutions.pose.Pose(stillImage,upperBody,smoothData,tol1,tol2)
        self.mpDraw=self.mp.solutions.drawing_utils
    def parseLandMarks(self,frame):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.bodyDetect.process(frameRGB)
        myBody=[]
        if results.pose_landmarks != None:
            self.mpDraw.draw_landmarks(x,results.pose_landmarks,self.mp.solutions.pose.POSE_CONNECTIONS)
            for LandMark in results.pose_landmarks.landmark:
                myBody.append((int(LandMark.x*width),int(LandMark.y*height)))
        return myBody

class mpHands:
    x=np.zeros([height,width,3],dtype=np.uint8)
    x[:,:]=(0,0,0)
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=.5,tol2=.5):
        self.handsDetect=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
        self.mpDraw=self.mp.solutions.drawing_utils
    def parseLandMarks(self,frame):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.handsDetect.process(frameRGB)
        myHands=[]
        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(x,handLandMarks,self.mp.solutions.hands.HAND_CONNECTIONS)
                myHand=[]
                for LandMark in handLandMarks.landmark:
                    myHand.append((int(LandMark.x*width),int(LandMark.y*height)))
                myHands.append(myHand)
        return myHands

findHands=mpHands(2)
findBody=mpBody()

while True:
    ignore,frame=cam.read()
    x=np.zeros([height,width,3],dtype=np.uint8)
    x[:,:]=(0,0,0)
    myHands=findHands.parseLandMarks(frame)
    myBody=findBody.parseLandMarks(frame)
    #if len(myBody)!=0:
        #cv2.circle(x,myBody[0],150,(0,255,0),2)
    #if len(myHands)!=0:
        #for oneHand in myHands:
            #for fingerTip in [4,8,12,16,20]:
                #cv2.circle(x,oneHand[fingerTip],25,(255,255,255),3)
    cv2.imshow('my Cam',x)
    cv2.moveWindow('my Cam',0,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()    
cv2.destroyAllWindows()