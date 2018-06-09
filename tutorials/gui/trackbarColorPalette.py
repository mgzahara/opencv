import numpy as np
import cv2

def nothing(x):
    pass

#create a black image
img = np.zeros((450, 600, 3), np.uint8)
#create a window
cv2.namedWindow('image')

#create trackbars for color selection
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

#create switch for on/off functionality
switch = '0 : OFF \n\t\t\t\t\t\t\t\t1 : ON '
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break


    # get current positions of the four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')


    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
        
cv2.destroyAllWindows()
