import numpy as numpy
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in i] # all events available in cv2 library
#print(events)

def click_event(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        string = "x: " + str(x)  + " y: " + str(y)
        print(x,', ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        one = cv2.putText(img,string,(x,y),font,2,(255,0,0),2)
        cv2.imshow('frame',one)
    if event == cv2.EVENT_MBUTTONDBLCLK:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', '+ str(green) + ', ' + str(red)
        one = cv2.putText(img,strBGR,(x,y),font,2,(255,0,0),2)
        cv2.imshow('frame',one)


cap = cv2.VideoCapture(0)

cap.set(3,1280)
cap.set(4,720)
old_x = 0
old_y =0

while(cap.isOpened()): #cap.IsOpened true when file open
    ret,frame = cap.read()
    if ret ==True:
        #print(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # frame count
        #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # frame height
        #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #frame width
        
        
        if frame is not None:
            
            img = frame
            #img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #convert bgr to gray
            cv2.imshow('frame',frame)
            cv2.setMouseCallback('frame',click_event)
            #out.write(gray)
            if (cv2.waitKey(100)  & 0xFF == ord('q')): #if q is pressed exit
                break
        
    else:
        break

cap.release()
cv2.destroyAllWindows()
