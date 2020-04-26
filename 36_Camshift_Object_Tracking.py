import numpy as np
import cv2

cap = cv2.VideoCapture('./data/traffic.mp4')
ret,frame = cap.read()
frame = cv2.resize(frame, (640, 640))
x, y, w, h = 220, 325, 150, 150
track_window = (x, y, w, h)

roi = frame[y:y + h, x:x + w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

#to avoid low range light
mask = cv2.inRange(hsv_roi,np.array((60.,30.,30.)),np.array((180.,255.,255)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
#cv2.imshow('roi', roi)
#cv2.imshow('roih', roi_hist)

#termination criteria either 10 iter or move by 1 point
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT , 10,1)
while(cap.isOpened()):
    ret,frame = cap.read()
    frame = cv2.resize(frame, (640, 640))
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

        #apply meanshift to get new location
        ret, track_window = cv2.CamShift(dst,track_window, term_criteria)

        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)

        final_image = cv2.polylines(frame, [pts], True, (0,255,0),2)
        #x,y,w,h = track_window
        #final_image = cv2.rectangle(frame, (x,y),(x+w,y+h),255,3)
        #cv2.imshow('dst', dst)
        cv2.imshow('frame',final_image)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break

cv2.destroyAllWindows()
cap.release()
