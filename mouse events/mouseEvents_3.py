import numpy as np
import cv2


events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def clk_evnt(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        colorImg = np.zeros((512, 512, 3), np.uint8)
        colorImg[:] = [blue, green, red]
        cv2.imshow('color',colorImg)

       


img = cv2.imread('lena.jpg', 1)
cv2.imshow('Mouse events_3', img)
points = []


cv2.setMouseCallback('Mouse events_3', clk_evnt)
cv2.waitKey(0)
cv2.destroyAllWindows() 
