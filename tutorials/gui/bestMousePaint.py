import cv2
import numpy as np
import random

def r(a, b):
    return (random.randint(a, b),random.randint(a, b),random.randint(a, b))
def nothing(a):
    pass
#curr_img is active drawing layer
#base_img is the canvas
#blen_img is used for display of both simultaneously

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
#color = (0, 0, 0)# init color - black
circles = [] # maintain all current circles to draw upon LBUTTONUP

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix, iy, drawing, mode, color, curr_img, base_img, circles
    mode = cv2.getTrackbarPos(shape, 'image') == 0
    color = (cv2.getTrackbarPos('B','image'), cv2.getTrackbarPos('G','image'), cv2.getTrackbarPos('R','image'))
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        curr_img = np.zeros((512,512,3), np.uint8)

    elif event == cv2.EVENT_MOUSEMOVE:
        #draw on preview layer
        if drawing == True:
            if mode == True:
                curr_img = np.zeros((512,512,3), np.uint8)
                cv2.rectangle(curr_img,(ix,iy),(x,y),color,-1)
            else:
                cv2.circle(curr_img,(x,y),5,color,-1)
                circles.append((x,y))

    elif event == cv2.EVENT_LBUTTONUP:
        #finalize drawings onto base_img
        drawing = False
        if mode == True:
            cv2.rectangle(base_img,(ix,iy),(x,y),color,-1)
        else:
            for coor in circles:
                cv2.circle(base_img,coor,5,color,-1)
            cv2.circle(base_img,(x,y),5,color,-1)
            circles = []


base_img = np.zeros((512,512,3), np.uint8)
blen_img = np.zeros((512,512,3), np.uint8)
curr_img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

#create sliders
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)
shape = '0: Rect\n1: Circ'
cv2.createTrackbar(shape, 'image', 0, 1, nothing)


while(1):
    if drawing:
        blen_img = cv2.addWeighted(base_img,0.3,curr_img,0.7,0) # layer the two images
        cv2.imshow('image', blen_img)
    else:
        cv2.imshow('image',base_img)
    k = cv2.waitKey(1) & 0xFF

    if k == ord('c'):
        #change color
        ran = r(0,255)
        cv2.setTrackbarPos('R', 'image', ran[0])
        cv2.setTrackbarPos('G', 'image', ran[1])
        cv2.setTrackbarPos('B', 'image', ran[2])
    elif k == 27:
        #ESC -> end
        break

cv2.destroyAllWindows()
