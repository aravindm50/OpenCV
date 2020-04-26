import numpy as np
import cv2

img = cv2.imread('./data/opencv-logo.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,127,255,0)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

#contour = python list of image, each contour is a numoy array of (x,y) boundary points
#hierarcy = optional output containing image topology

print("Number of contours = " + str(len(contours)))

#drawing contours
# -1 cotour idx gives all contours
cv2.drawContours(img,contours, 8,(0,255,255),3)
cv2.imshow('color',img)
cv2.imshow('gray',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()