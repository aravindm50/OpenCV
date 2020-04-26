import cv2

cap = cv2.VideoCapture(0); #o is the index of the default device

fourcc = cv2.VideoWriter_fourcc(*'XVID') # fourcc codes can be obtained from www.fourcc.org/codecs.php
#fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480)) # video writer to file specified, 20.0 is the number of frames to be saved, 640*480 is the frame size
print(cap.isOpened())
while(cap.isOpened()): #cap.IsOpened true when file open
    ret,frame = cap.read()
    if ret ==True:
        print(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # frame count
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # frame height
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #frame width

        out.write(frame)
        if frame is not None:
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #convert bgr to gray
            cv2.imshow('frame',gray)

            if cv2.waitKey(1) & 0xFF == ord('q'): #if q is pressed exit
                break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()