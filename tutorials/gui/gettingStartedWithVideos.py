import numpy as np
import cv2

cap = cv2.VideoCapture(0)

#stream video from camera to window, frame by frame
##no saving, just accessing the camera

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break #stream frames until 'q' key is pressed
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

#play video from file

vidFile = "/home/matt/OpenCV/samples/data/vtest.avi"
cap2 = cv2.VideoCapture(vidFile)

while(cap2.isOpened()):
    ret, frame = cap2.read()
    try:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    except Error:
        pass
    
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
