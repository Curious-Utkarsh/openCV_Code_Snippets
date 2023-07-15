import cv2
print(cv2.__version__)
import mediapipe as mp

width=1280
height=720

cam=cv2.VideoCapture(1, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

faceMesh = mp.solutions.face_mesh.FaceMesh(False,2,.5,.5)
mpDraw = mp.solutions.drawing_utils

while True:
    ignore,frame=cam.read()
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=faceMesh.process(frameRGB)
    #print(results.multi_face_landmarks)
    if results.multi_face_landmarks != None:
        for faceLandmarks in results.multi_face_landmarks:
            #mpDraw.face_landmarks(frame,faceLandmarks)
            mpDraw.draw_landmarks(frame,faceLandmarks,mp.solutions.face_mesh.FACE_CONNECTIONS)

    cv2.imshow('my Cam',frame)
    cv2.moveWindow('my Cam',0,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()    
cv2.destroyAllWindows()
