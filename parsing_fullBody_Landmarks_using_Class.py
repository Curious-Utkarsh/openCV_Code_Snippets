import cv2
print(cv2.__version__)

width=1280
height=720

cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

class mpBody:
    import mediapipe as mp
    def __init__(self,stillImage=False,upperBody=False,smoothData=True,tol1=.5,tol2=.5):
        self.bodyDetect=self.mp.solutions.pose.Pose(stillImage,upperBody,smoothData,tol1,tol2)
        self.mpDraw=self.mp.solutions.drawing_utils
    def parseLandMarks(self,frame):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.bodyDetect.process(frameRGB)
        myBody=[]
        if results.pose_landmarks != None:
            self.mpDraw.draw_landmarks(frame,results.pose_landmarks,self.mp.solutions.pose.POSE_CONNECTIONS)
            for LandMark in results.pose_landmarks.landmark:
                myBody.append((int(LandMark.x*width),int(LandMark.y*height)))
        return myBody

findBody=mpBody()

while True:
    ignore,frame=cam.read()
    myBody=findBody.parseLandMarks(frame)
    if len(myBody)!=0:#prevents program from crashing when it doesnot detect any body or hand or any other landmarks
        for i in [0,2,5]:
            cv2.circle(frame,myBody[i],20,(0,255,255),2)    
    cv2.imshow('my Cam',frame)
    cv2.moveWindow('my Cam',0,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()    
cv2.destroyAllWindows()
