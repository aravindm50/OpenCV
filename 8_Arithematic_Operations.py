import cv2
import numpy as np

img = cv2.imread('./data/lena.jpg')
img2 = cv2.imread('./data/messi5.jpg')

print(img.shape)
print(img.size)
print(img.dtype)

b,g,r, = cv2.split(img)

img = cv2.merge((b,g,r))

eye = img[252:274,270:288]

img[252:274,300:318] = eye

#resizing images to add them
img = cv2.resize(img,(200,200))
img2 = cv2.resize(img2, (200,200))

img3 = cv2.add(img,img2)

img4 = cv2.addWeighted(img,0.9, img2, 0.1,-1)

cv2.imshow('image',img3)
cv2.imshow('image1',img4)
cv2.waitKey(10000)
cv2.destroyAllWindows()