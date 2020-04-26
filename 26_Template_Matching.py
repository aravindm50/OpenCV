import cv2
import numpy as np

img = cv2.imread('./data/messi5.jpg')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = imgGrey[60:130,203:263]

res = cv2.matchTemplate(imgGrey,template, cv2.TM_CCOEFF_NORMED)
print(res)

thresh = 0.9;

loc = np.where(res >= thresh)
print(loc)

w,h = template.shape[::-1]

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w,pt[1] + h),(255,0,0),2)

cv2.imshow('img',img)
cv2.imshow('img2',template)
cv2.waitKey(0)
cv2.destroyAllWindows()