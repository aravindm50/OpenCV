import cv2
import numpy as np

img = cv2.imread('./data/sudoku.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize=3)
cv2.imshow('edges',edges)
#hough lines
#rhp = distance resolution of the accumulator in pixels
#thetha = angle resolution of the accumulator in radians
#threshold = accumulator threshold parameter to filter out lines above threshold
lines = cv2.HoughLines(edges,1,np.pi/180,200)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    #x1 stores the rounded off value of (r*cos(theta) - 1000 * sin(theta))
    x1 = int(x0 + 1000 *(-b))
    # y1 stores the rounded off value of (r*sin(theta) + 1000 * cos(theta))
    y1 = int(y0 + 1000 * (a))
    # x2 stores the rounded off value of (r*cos(theta) + 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b))
    # y2 stores the rounded off value of (r*sin(theta) - 1000 * cos(theta))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
