import cv2
import face_recognition as FR
import pickle

print(cv2.__version__)

#rb stands for Read Binary
with open('KJ_FACE_ENCODINGS.pkl','rb') as f:
    names=pickle.load(f)
    faceLoc=pickle.load(f)
    knownEncodings=pickle.load(f)

unknownPic=FR.load_image_file('C:/Users/kutka/Documents/python/Faces_Database_KJ/unknownPics/p2.jpeg')
FaceLocations=FR.face_locations(unknownPic)
unknownEncodings=FR.face_encodings(unknownPic,FaceLocations)
unknownPicBGR=cv2.cvtColor(unknownPic,cv2.COLOR_RGB2BGR)

for FaceLocation,unknownEncoding in zip(FaceLocations,unknownEncodings):
    top,right,bottom,left=FaceLocation
    name='Unknown Person'
    cv2.rectangle(unknownPicBGR,(right,top),(left,bottom),(255,0,0),3)
    matches=FR.compare_faces(knownEncodings,unknownEncoding)
    if True in matches:
        matchIndex=matches.index(True)
        name=names[matchIndex]
    cv2.putText(unknownPicBGR,name,(left,top),cv2.FONT_HERSHEY_COMPLEX,.5,(0,0,255),2)
cv2.imshow('My UnknownPic',unknownPicBGR)
cv2.moveWindow('My UnknownPic',0,0)
cv2.waitKey(5000)
cv2.destroyAllWindows()