from os import listdir
from os.path import isfile, join
import imghdr
import sys
import numpy as np
import cv2

window_width    = 600
window_height   = 600
window_name     = "Slideshow"
img_wait_time   = 1500
alpha_inc       = 0.05
transition_wait = 75

def transition(img1, img2):
    #fade from img1 to img2
    alpha = 0
    while alpha < 1:
        res = cv2.addWeighted(img1, 1 - alpha, img2, alpha, 0)
        cv2.imshow(window_name, res)
        cv2.waitKey(transition_wait) #wait 100 ms
        alpha += alpha_inc #inc alpha  

def slideshow(img1path, img2path):
    #prepare the images for transition
    img1 = cv2.imread(img1path)
    img2 = cv2.imread(img2path)

    #images must be the same dimensions to use addWeighted()
    resized1 = cv2.resize(img1, (window_width, window_height), interpolation = cv2.INTER_AREA)
    resized2 = cv2.resize(img2, (window_width, window_height), interpolation = cv2.INTER_AREA)
    
    cv2.imshow(window_name, resized1)
    cv2.waitKey(img_wait_time)
    transition(resized1, resized2)
    cv2.imshow(window_name, resized2)
    cv2.waitKey(img_wait_time)

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
mypath=sys.argv[1]
print
print "mypath: ", mypath
print
supported=['pbm', #acceptable img formats
           'pgm', 
           'ppm', 
           'tiff',
           'rast', 
           'jpeg', 
           'bmp', 
           'png']
toDisplay=[]

#courtesy of Arshin on StackOverflow
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print
#print "files:"
#for f in files:
#    print f
#print
for f in files:
    if imghdr.what(mypath+f) in supported:
        toDisplay.append(f)

toDisplay.sort()
for d in range(len(toDisplay) - 1):
    print "displaying ", toDisplay[d]
    slideshow(mypath + toDisplay[d], mypath + toDisplay[d+1])
cv2.destroyAllWindows()
