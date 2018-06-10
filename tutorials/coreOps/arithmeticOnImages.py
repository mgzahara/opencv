import time
import numpy as np
import cv2

#intro to manipulating images

img1 = cv2.imread("/home/matt/OpenCV/samples/data/messi5.jpg")
img2 = cv2.imread("/home/matt/OpenCV/samples/data/WindowsLogo.jpg")
logo = cv2.imread("/home/matt/OpenCV/samples/data/opencv-logo.png")

img1Shape = img1.shape
img2Shape = img2.shape

print "img1: ", img1Shape
print "img1: ", img2Shape
#make both images the same dimensions
x = min(img1Shape[0], img2Shape[0])
y = min(img1Shape[1], img2Shape[1])
resized1 = img1[:x, :y]
resized2 = img2[:x, :y]

print "resized img1: ", resized1.shape
print "resized img2: ", resized2.shape

res1 = cv2.add(resized1, resized2) #washed out - all RGB value are added, so they are all higher resulting in more white
res2 = resized1 + resized2 #doesnt do anything helpful

#IMAGE BLENDING
dst = cv2.addWeighted(resized1, 0.2, resized2, 0.8, 0) #actual merging of images, the weights must add to 1, the higher is more prominent in result

cv2.imshow("cv2 added", res1)
k = cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imshow("numpy added", res2)
k = cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imshow("cv2 blended", dst)
k = cv2.waitKey(0)

cv2.destroyAllWindows()
