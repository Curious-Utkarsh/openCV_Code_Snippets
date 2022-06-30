import cv2
import face_recognition as FR
import time
print(cv2.__version__)

font=cv2.FONT_HERSHEY_COMPLEX
width=320
height=240
cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
#cam.set(cv2.CAP_PROP_FPS, 120)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

utkFace=FR.load_image_file('C:/Users/kutka/Documents/python/Faces_Database_KJ/knownFaces/Kumar Utkarsh.jpeg')
utkFaceLoc=FR.face_locations(utkFace)[0]
utkFaceEncoding=FR.face_encodings(utkFace)[0]

nimFace=FR.load_image_file('C:/Users/kutka/Documents/python/Faces_Database_KJ/knownFaces/Nimish Tiwari.jpeg')
nimFaceLoc=FR.face_locations(nimFace)[0]
nimFaceEncoding=FR.face_encodings(nimFace)[0]

knownEncodings=[utkFaceEncoding,nimFaceEncoding]
names=['UTKARSH','NIMISH']

tlast=time.time()
time.sleep(1)

while True:
    ignore,unknownFace=cam.read()
    dT=time.time()-tlast
    fps=int(1/dT)
    print(fps)
    tlast=time.time()
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
