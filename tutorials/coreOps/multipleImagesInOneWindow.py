import numpy as np
import cv2

#def imshow_delay(title, img, delay):
#    cv2.imshow(title, img)
#    cv2.waitKey(delay)
def transition(img1, img2):
    alpha = 0
    while alpha < 1:
        res = cv2.addWeighted(img1, 1 - alpha, img2, alpha, 0)
        cv2.imshow('transition', res)
        cv2.waitKey(100)#wait 100 ms
        alpha += 0.05#inc alpha
    

img1 = cv2.imread("/home/matt/OpenCV/samples/data/messi5.jpg")
img2 = cv2.imread("/home/matt/OpenCV/samples/data/HappyFish.jpg")

img1Shape = img1.shape
img2Shape = img2.shape

#print "img1: ", img1Shape
#print "img1: ", img2Shape
#make both images the same dimensions
x = min(img1Shape[0], img2Shape[0])
y = min(img1Shape[1], img2Shape[1])
resized1 = img1[:x, :y]
resized2 = img2[:x, :y]

cv2.namedWindow('transition')
#show img1
cv2.imshow('transition', resized1)
cv2.waitKey(2000)
#transition
transition(resized1, resized2)
#show img2
cv2.imshow('transition', resized2)
cv2.waitKey(2000)
cv2.destroyAllWindows()



