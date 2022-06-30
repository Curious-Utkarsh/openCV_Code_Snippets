#KJ FACE ENCODINGS
import cv2
import face_recognition as FR
import os
import pickle

print(cv2.__version__)

names=[]
faceLoc=[]
knownEncodings=[]

imageDir=('C:\\Users\kutka\Documents\python\Faces_Database_KJ')

for root,dirs,files in os.walk(imageDir):
    #print('My Working Folder(root) : ',root)
    #print('Available Directories : ',dirs)
    #print('My Files : ',files)
    for file in files:
        #print('Your File is : ',file)
        imageFullPath=os.path.join(root,file)
        #print('File Full Path : ',imageFullPath)
        personName=os.path.splitext(file)[0]
        #print('Person Name : ',personName)
        myPic=FR.load_image_file(imageFullPath)
        myPicLoc=FR.face_locations(myPic)[0]
        myPicEncoding=FR.face_encodings(myPic)[0]

        names.append(personName)
        faceLoc.append(myPicLoc)
        knownEncodings.append(myPicEncoding)

with open('KJ_FACE_ENCODINGS.pkl','wb') as f:
    pickle.dump(names,f)
    pickle.dump(faceLoc,f)
    pickle.dump(knownEncodings,f)
#wb stands for Write Binary    