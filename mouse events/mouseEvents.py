import numpy as np  
import cv2


events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def clk_evnt(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        font  = cv2.FONT_HERSHEY_SIMPLEX
        strXY =str(x) +', ' + str(y)
        cv2.putText(img, strXY, (x,y), font, 0.5, (255,255,255), 2)
        cv2.imshow('White: X-Y co-ords, Cyan: RGB values', img)
        
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font  = cv2.FONT_HERSHEY_SIMPLEX
        strBGR =str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x,y), font, 0.5, (255,255,0), 2)
        cv2.imshow('White: X-Y co-ords, Cyan: RGB values', img)

#img = np.zeros((512, 512, 3), np.uint8)
img =  cv2.imread ('lena.jpg', 1)
cv2.imshow('White: X-Y co-ords, Cyan: RGB values', img)



cv2.setMouseCallback('White: X-Y co-ords, Cyan: RGB values', clk_evnt)
cv2.waitKey(0)
cv2.destroyAllWindows() 
