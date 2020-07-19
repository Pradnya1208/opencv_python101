import numpy as np
import cv2

#img = cv2.imread('lena.jpg',1)
img = np.zeros((512,512,3), np.uint8) 



#parameters(image, starting co-ordinates, ending co-ordinates, BGR, thickness)
img = cv2.line(img , (0,0), (255 ,255), (255, 0, 0), 5)
img = cv2.arrowedLine(img , (0,255), (255 ,255), (0, 0, 255), 5)

#rectangle : parameters(image, topleft vertex co-ordinates, lower vertex co-ordinates, BGR, thickness)
img  = cv2.rectangle(img, (380,40), (500,120), (0, 255, 0), -1) #-1 :to fill the color

#circle : parameters (iamage, center of the cicle, radius, BGR, thickness)
img = cv2.circle(img, (400,400),60,(120, 40, 100), -1)

#Text: parameters(image, text, co-ordinates, font, fontsize, color, thickness, line type)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "Geometric patterns",(30,30), font, 1, (255,255,255), 2, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0) & 0xFF



cv2.destroyAllWindows()
