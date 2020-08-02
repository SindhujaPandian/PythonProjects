import os
import cv2

path = os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(path)

Eyepath = os.path.dirname(cv2.__file__)+"/data/haarcascade_eye.xml"
eyeCascade = cv2.CascadeClassifier(Eyepath)
first_read=True
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.1,minNeighbors = 5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)

    if(len(faces)>0):
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y) , (x+w,y+h), (0,255,0), 2)
            ROI_gray = gray[y:y+h , x: x+w]
            ROI_img = frame[y:y+h , x: x+w]

            eye = eyeCascade.detectMultiScale(ROI_gray)
            if(len(eye)>=2): 
                #Check if program is running for detection  
                if(first_read): 
                    cv2.putText(frame,  
                    "Eye detected press s to begin",  
                    (70,70),   
                    cv2.FONT_HERSHEY_PLAIN, 3, 
                    (0,255,0),2)
                    first_read=False
                else: 
                    cv2.putText(frame,  
                    "Eyes open!", (70,70),  
                    cv2.FONT_HERSHEY_PLAIN, 2, 
                    (255,255,255),2) 
            else: 
                if(first_read): 
                    #To ensure if the eyes are present before starting 
                    cv2.putText(frame,  
                    "No eyes detected", (70,70), 
                    cv2.FONT_HERSHEY_PLAIN, 3, 
                    (0,0,255),2) 
                else: 
                    #This will print on console and restart the algorithm 
                    print("Blink detected--------------") 
                    cv2.waitKey(3000) 
                    first_read=True
            for (eye_x_cord,eye_y_cord,eye_width,eye_height) in eye:
                cv2.rectangle(ROI_img, (eye_x_cord,eye_y_cord), (eye_x_cord+eye_width,eye_y_cord+eye_height),(255,0,0),3)

    else:
        cv2.putText(frame, "No Face Detected", (100,100) , cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255),2)
    cv2.imshow('Video',frame)

    if cv2.waitKey(0) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
    
    
