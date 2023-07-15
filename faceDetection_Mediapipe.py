import cv2
print(cv2.__version__)

Width=640
Height=360

cam=cv2.VideoCapture(1,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,Width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,Height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

class mpFace:
    import mediapipe as mp
    def __init__(self):
        self.findFace=self.mp.solutions.face_detection.FaceDetection()
    def parseFaceBox(self,frame):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.findFace.process(frameRGB)
        if results.detections != None:
            for face in results.detections:
                myFace=[]
                faceBox = face.location_data.relative_bounding_box
                topLeft = (int(faceBox.xmin*Width),int(faceBox.ymin*Height))
                w = int(faceBox.width*Width)
                h = int(faceBox.height*Height)
                topRight = ((int(faceBox.xmin*Width)+w),(int(faceBox.ymin*Height)+h))
                myFace.append((topLeft,topRight))       
        return myFace

findFace=mpFace()

while True:
    ignore,frame=cam.read()
    myFaces=findFace.parseFaceBox(frame)
    for face in myFaces:
        cv2.rectangle(frame,face[0],face[1],(0,0,0),3)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()    

