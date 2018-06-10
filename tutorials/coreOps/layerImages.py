import numpy as np
import cv2

#layer a non-rectangular image over another - one w/o a background
#each step is illustrated

def imshow(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#img2 is going to be put in the top let corner of img1
#img2 must have less than or equal dimensions as img1 or it will fail:
#OpenCV(3.4.1) Error: Assertion failed ((mtype == 0 || mtype == 1) && _mask.sameSize(*psrc1)) in binary_op, file arithm.cpp, line 241

img1 = cv2.imread("/home/matt/OpenCV/samples/data/messi5.jpg")
img2 = cv2.imread("/home/matt/OpenCV/samples/data/smaller_opencv_logo.png")

#originals
imshow("soccer", img1)
imshow("logo", img2)


# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
imshow("img2gray", img2gray)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
imshow("mask", mask)
mask_inv = cv2.bitwise_not(mask)
imshow("mask_inv", mask_inv)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
imshow("img1_bg", img1_bg)
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
imshow("img2_fg", img2_fg)
# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
imshow("dst", dst)
img1[0:rows, 0:cols ] = dst
imshow("end result", img1)
