#Arithmatic operations on Images
#1. ROI: region of Interest of an Image
#2. add and addWeighted methods

import numpy as np
import cv2

img0 = cv2.imread('messi.jpg',1)
img1 = cv2.imread('messi.jpg',1)

img = cv2.imread('messi.jpg',1)
img2 = cv2.imread('opencv-logo.png',1)



print ("Image Shape: " + str(img.shape) + ", Image size: " + str(img.size) + ", datatype: " + str(img.dtype))
b,g,r = cv2.split(img)
img1 = cv2.merge((b,g,r))


#get the coordinates (frm the mouse click event code)of the football(ROI in the image)
ball = img1[280:340, 330:390]
img1[273:333, 100:160] = ball


#merging of 2 images with add and addWeighted methods
img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2,(512,512))

#dest = cv2.add(img,img2)
dest = cv2.addWeighted(img, 0.9, img2, 0.1, 0)


cv2.imshow('Original Image',img0)
cv2.imshow('Image',img1)

cv2.imshow('logo',img2)
cv2.imshow('Merged images',dest)
cv2.waitKey(0)
cv2.destroyAllWindows()
