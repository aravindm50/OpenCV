import cv2
import datetime


cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#cap.set(cv2.CAP_PROP_FRAME_WIDTH,500)
# can be set using the proert number also
cap.set(3,1280)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT,500)
cap.set(4,720)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(cap.isOpened())
while(cap.isOpened()): #cap.IsOpened true when file open
    ret,frame = cap.read()
    if ret ==True:
        #print(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # frame count
        #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # frame height
        #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #frame width
        
        
        if frame is not None:
            
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #convert bgr to gray

            font = cv2.FONT_HERSHEY_SIMPLEX
            gray = cv2.putText(gray,"Width: " +str(cap.get(3)) + ' Height: '+ str(cap.get(4)) + ' Date:' + now,(20,20),font,1,(0,255,255),3)
            cv2.imshow('frame',gray)
            #out.write(gray)
            if cv2.waitKey(1) & 0xFF == ord('q'): #if q is pressed exit
                break
        
    else:
        break

cap.release()
cv2.destroyAllWindows()