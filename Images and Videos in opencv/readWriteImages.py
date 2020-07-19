import cv2

#Read image with Flag = 1:loads color image, 0: Grayscale mode, -1:alpha channel 
img =  cv2.imread ('lena.jpg', 1)
print(img)

#display image
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF

#write image
if k == 27:  #Esc key
    cv2.destroyAllWindows()

elif k ==ord('s'):
    cv2.imwrite('lena_copy.png',img)
    cv2.destroyAllWindows()

else:
    cv2.destroyAllWindows()
