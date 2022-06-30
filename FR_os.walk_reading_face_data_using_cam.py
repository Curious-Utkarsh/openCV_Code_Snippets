import cv2
import face_recognition as FR
import pickle
print(cv2.__version__)

font=cv2.FONT_HERSHEY_COMPLEX
width=1280
height=720
cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

with open('KJ_FACE_ENCODINGS.pkl','rb') as f:
    names=pickle.load(f)
    faceLoc=pickle.load(f)
    knownEncodings=pickle.load(f)

while True:
    ignore,unknownFace=cam.read()
    unknownFace=cv2.resize(unknownFace,(320,180))
    unknownFaceRGB=cv2.cvtColor(unknownFace,cv2.COLOR_BGR2RGB)
    unknownFaceLocs=FR.face_locations(unknownFaceRGB)
    unknownFaceEncodings=FR.face_encodings(unknownFaceRGB,unknownFaceLocs)

    for unknownFaceLoc,unknownFaceEncoding in zip(unknownFaceLocs,unknownFaceEncodings):
        name='Unknown Person'
        top,right,bottom,left=unknownFaceLoc
        cv2.rectangle(unknownFace,(left,top),(right,bottom),(0,0,255),3)
        matches=FR.compare_faces(knownEncodings,unknownFaceEncoding)
        if True in matches:
            matchIndex=matches.index(True)
            name=names[matchIndex]
        cv2.putText(unknownFace,name,(left,top),font,1,(0,255,0),2)
    cv2.imshow('my WEBcam',unknownFace)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()  
cv2.destroyAllWindows()  
