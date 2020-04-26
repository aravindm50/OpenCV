import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in i] # all events available in cv2 library
#print(events)

'''def click_event(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img,points[-1],points[-2],(0,255,255),5)
        cv2.imshow('frame',img)'''

def click_event(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        cv2.imshow('frame',img)
        mycolor = np.zeros((255,255,3),np.uint8)
        mycolor[:]=[blue,green,red]
        cv2.imshow('color',mycolor)



cap = cv2.VideoCapture(0)

#cap.set(3,1280)
#cap.set(4,720)
old_x = 0
old_y =0
points = []
while(cap.isOpened()): #cap.IsOpened true when file open
    ret,frame = cap.read()
    if ret ==True:
        #print(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # frame count
        #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # frame height
        #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #frame width
        
        
        if frame is not None:
            
            img = frame
            #img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #convert bgr to gray
            cv2.imshow('frame',img)
            cv2.setMouseCallback('frame',click_event)
            #out.write(gray)
            if (cv2.waitKey(10)  & 0xFF == ord('q')): #if q is pressed exit
                break
        
    else:
        break

cap.release()
cv2.destroyAllWindows()
