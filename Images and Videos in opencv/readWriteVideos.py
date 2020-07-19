#Topics covered:
#1.Capture video
#2.Saving video
#3.Setting parameters such as height and width of frame
#4.Showing Date and Time and some other text parameters on Video frame 

import cv2
import datetime

#0 - camera source,  we can also give pre-existing video as input
cap = cv2.VideoCapture(0)

# setting parameters
#cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)


#to save the video
#fourCC code to identify the format
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#arguements- (filename, fourcc, no.of frames, width-height)
output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480)) 


#use cap.isOpened in case of prexisting video
while True: 
    ret, frame = cap.read()
    
    if ret == True:
    
        #get method to get properties of frame
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #parameter number is 3
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #parameter number is 4

       

        
        #writing a frame into a file
        output.write(frame)

        #convert to gray scle
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('frame', gray)

        font  = cv2.FONT_HERSHEY_SIMPLEX
        text = "Width: " + str(cap.get(3)) + " Height: " + str(cap.get(4))
        dt = str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (30,30), font, 1, (255,255,255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, dt, (10,460), font, 0.5, (255,255,255), 1, cv2.LINE_AA)
        cv2.imshow('frame', frame)
   
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
output.release()
cv2.destroyAllWindows()

    
