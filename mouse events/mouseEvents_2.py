import numpy as np  
import cv2


events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def clk_evnt(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
       cv2.circle(img, (x, y), 10 , (255,255,0), -1)
       points.append((x,y))
       if  len(points) >= 2:
           cv2.line(img, points[-1], points[-2], (0,255,0),5)
       cv2.imshow('Mouse events_2', img)

       


img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('Mouse events_2', img)
points = []


cv2.setMouseCallback('Mouse events_2', clk_evnt)
cv2.waitKey(0)
cv2.destroyAllWindows() 
