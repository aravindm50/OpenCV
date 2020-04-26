import numpy as np
import cv2

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                                   (3,3))
cap = cv2.VideoCapture('./data/Megamind.avi')
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
fgbg1 = cv2.createBackgroundSubtractorKNN()
while(cap.isOpened()):
    ret,frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    fgmask1 = fgbg1.apply(frame)
    fgmask1 = cv2.morphologyEx(fgmask1,cv2.MORPH_OPEN,kernel=kernel)
    cv2.imshow('Frame',frame)
    cv2.imshow('FG Mask', fgmask)
    cv2.imshow('FG Mask 2', fgmask1)

    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()