import numpy as np
import cv2

img = cv2.imread('./data/smarties.png')
output = img.copy()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,5)

#Hough Circles:
# image = 8 bit singe channel image
# circles = output vector of found circles
# method = detection method, hough modes
# dp = inverse ratio of accumulator resolution to image resolution
# mindist = minimum distance between the center of detected circles
# param1 = first method specific parameter. In case of Hough Gradient, it is
# higher threshold of the two passed to canny edge detector. (Lower one is
# twice smaller)
# param2 = Second method specific parameter. In case of hough gradient,
# it is the accumulator threshold for the circle centers at the detection stage
#minRadius = Minimum circle radius
#maxRadius = Maximum circle radius If <= 0, uses maximum image dimension.
# If < 0, returns centers without finding the radius.
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1, 20, param1= 50,
                           param2= 30,
                           minRadius= 0,
                           maxRadius= 0)

detected_circles = np.uint16(np.around(circles))
for (x,y,r) in detected_circles[0,:]:
    cv2.circle(output,(x,y),r,(255,0,0),2)
    cv2.circle(output, (x, y), 2, (255, 255, 0), 2)

cv2.imshow('image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
