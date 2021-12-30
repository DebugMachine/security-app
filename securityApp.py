from os import access
import cv2, dropbox, random, time

def take_snapshot():
    videoCaptureObject = cv2.VideoCapture(0) #This will start the webcam and the 0 repersents the webcam of the system
    result = True

    while (result):
        number = random.randint(0,100)
        bool,frame = videoCaptureObject.read() #Read is a function which reads the frames while the camera is on.
                                              #VideoCaptureObject.read is reading 2 values at the same time.   
        print(frame)
        picture = "NewImg"+str(number)+".jpg"
        cv2.imwrite(picture,frame) # Cv2.imwrite is used to save any image to a storage.
        result = False 
        
    videoCaptureObject.release() #This method is used to release the camera/turn it off.
    cv2.destroyAllWindows() #Closes all the windows that might be open because of the camera.
    
    return picture

take_snapshot()


