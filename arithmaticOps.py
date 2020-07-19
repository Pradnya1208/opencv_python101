#Arithmatic operations on Images

import cv2

img = cv2.imread('messi.jpg',1)

print ("Image Shape: " + str(img.shape) + ", Image size: " + str(img.size) + ", datatype: " + str(img.dtype))
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))


cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
