import numpy as np
import cv2

img = cv2.imread('./data/chessboard.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('img',img)
#necessary to convert to float32 to use Harris corner method
gray = np.float32(gray)
#blocksize = it is the size of the neighbourhoood for corner detection
#ksize = aperture parameter of sobel derivative used
#k = harris detector free parameter in the equation
dst = cv2.cornerHarris(gray,2,3,0.04)

#to get better result dilate
dst = cv2.dilate(dst,None)

img[dst > 0.01 * dst.max()] = [0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xFF==ord('q'):
    cv2.destroyAllWindows()