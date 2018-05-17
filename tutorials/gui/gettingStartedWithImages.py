import numpy as np
import cv2
from matplotlib import pyplot as plt

validKey = False
imgDir = '/home/matt/OpenCV/samples/data/'
imgFile1 = imgDir + 'baboon.jpg'
imgFile2 = imgDir + 'baboon.jpg'

#the 0 as the second arg denotes opening the image as grayscale
img1 = cv2.imread(imgFile1, 0)
img2 = cv2.imread(imgFile1, 0)

cv2.imshow('baboon image', img1)

#display using matplotlib - this is the first GUI to display
#the validKey loop below is not relevent to this window
plt.imshow(img2, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

#loop until desired keys are pressed
while(not validKey):
    k = cv2.waitKey(0)
    validKey = True
    if k == 27:
        #escape key
        cv2.destroyAllWindows()
    elif k == ord('s'):
        #'s' key
        #save img as PNG in local dir
        cv2.imwrite('baboon_gray.png', img)
        cv2.destroyAllWindows()
    else:
        validKey = False
