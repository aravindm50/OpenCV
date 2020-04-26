import numpy as np
import cv2

img = cv2.imread('./data/pic1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('img',img)

corners = cv2.goodFeaturesToTrack(gray,50,0.01,10)
corners = np.int0(corners)


for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow('shitomasi',img)

gray = np.float32(gray)
#blocksize = it is the size of the neighbourhoood for corner detection
#ksize = aperture parameter of sobel derivative used
#k = harris detector free parameter in the equation
dst = cv2.cornerHarris(gray,2,3,0.04)

#to get better result dilate
dst = cv2.dilate(dst,None)

img[dst > 0.01 * dst.max()] = [0,0,255]
cv2.imshow('harris',img)
if cv2.waitKey(0) & 0xFF==ord('q'):
    cv2.destroyAllWindows()