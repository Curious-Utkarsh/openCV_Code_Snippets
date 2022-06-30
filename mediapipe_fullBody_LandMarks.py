import cv2
print(cv2.__version__)
import mediapipe as mp

width=1280
height=720

cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

poseDetect=mp.solutions.pose.Pose(False,False,.5,.5)
#poseDetect=mp.solutions.pose.Pose("Is it static Image"-FALSE,"Do you want Pose of only Upper Body"-if yes-TRUE, if want full body-FALSE,.5,.5)
mpDraw=mp.solutions.drawing_utils

while True:
    ignore,frame=cam.read()
    frame=cv2.flip(frame,1)
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=poseDetect.process(frameRGB)
    if results.pose_landmarks != None:
        mpDraw.draw_landmarks(frame,results.pose_landmarks,mp.solutions.pose.POSE_CONNECTIONS)
        #print(results.pose_landmarks)
        #print(results.pose_landmarks.landmark)
        myBody=[]
        for LandMark in results.pose_landmarks.landmark:
            myBody.append((int(LandMark.x*width),int(LandMark.y*height)))
        for i in [0,2,5]:
            cv2.circle(frame,myBody[i],20,(0,255,255),2)#Puts a circle on my nose and eyes
    cv2.imshow('my Cam',frame)
    cv2.moveWindow('my Cam',0,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()    
cv2.destroyAllWindows()