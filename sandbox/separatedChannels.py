import cv2
import numpy

src = cv2.imread("opencv_frame_0.png")

#slow
#b, g, r = cv2.split(src)

#better - get each channel as B/W
b = src[:, :, 0]
g = src[:, :, 1]
r = src[:, :, 2]


#get all red img
#filter out blue
src[:, :, 0] = 0
#filter out green
src[:, :, 1] = 0

#should be only red
cv2.imshow('test', src)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Mat bgr[3];  # //destination array
#split(src,bgr)#;//split source

#//Note: OpenCV uses BGR color order
#imwrite("blue.png",bgr[0])#; //blue channel
#imwrite("green.png",bgr[1])#; //green channel
#imwrite("red.png",bgr[2])#; //red channel
