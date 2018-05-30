import numpy as np
import cv2
import random

def r(a, b):
    return random.randint(a, b)

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img,(x,y),r(25, 100),(r(0, 255),r(0, 255),r(0, 255)),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        #ESC key
        break
cv2.destroyAllWindows()
