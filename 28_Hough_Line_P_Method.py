import cv2
import numpy as np

img = cv2.imread('./data/chessboard.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize=3)
cv2.imshow('edges',edges)
#hough lines
#rhp = distance resolution of the accumulator in pixels
#thetha = angle resolution of the accumulator in radians
#threshold = accumulator threshold parameter to filter out lines above threshold
lines = cv2.HoughLinesP(edges,1,np.pi/180,200)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
