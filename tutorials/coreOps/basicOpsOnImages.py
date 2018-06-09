import cv2
import numpy as np

img = cv2.imread("/home/matt/OpenCV/samples/data/messi5.jpg")

#ACCESS AND MODIFY PIXEL VALUES
#access a pixel
px = img[100, 100]
print "px: ", px

#access blue value of above pixel
blue = img[100, 100, 0]
print "blue: ", blue

#modify above pixel
img[100, 100] = [255, 255, 255]

#modify above blue value
img[100, 100, 0] = 255

#Note Above mentioned method is normally used for selecting a region of array, say first 5 rows and last 3 columns like that. For individual pixel access, Numpy array methods, array.item() and array.itemset() is considered to be better. But it always returns a scalar. So if you want to access all B,G,R values, you need to call array.item() separately for all.

#better pixel access
red = img.item(100, 100, 2)
print "better red access: ", red

#better modify - set red value of pixel 100, 100 to 210
img.itemset((100, 100, 2), 210)
print "modified red: ", img.item(100, 100, 2)


#ACCESS IMAGE PROPERTIES
#shape of image
print "shape: ", img.shape
#Note If image is grayscale, tuple returned contains only number of rows and columns. So it is a good method to check if loaded image is grayscale or color image.

#total number of pixels
print "num pixels: ", img.size

#image data type
print "image data type: ", img.dtype


#REGION OF IMAGE
#select a region
ball = img[280:340, 330:390]
#put it somewhere else
img[273:333, 100:160] = ball


#SPLITTING/MERGING IAMGE
#split into separate channels
b,g,r = cv2.split(img)
#merge channels into image
img = cv2.merge((b,g,r))

#using numpy - faster
b = img[:, :, 0]
#set all red values to 0
img[:, :, 2] = 0


BLUE = [255, 0, 0]

replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
#no border
cv2.imshow("no border", img)
while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
#replicate border
cv2.imshow("replicate", replicate)
while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
#reflect border
cv2.imshow("reflect", reflect)
while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
#reflect101 border
cv2.imshow("reflect101", reflect101)
while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
#wrap border
cv2.imshow("wrap", wrap)
while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
#constant border
cv2.imshow("constant", constant)
while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
