import numpy as np
import cv2

from matplotlib import pyplot as plt

img = cv2.imread('./data/messi5.jpg',0)

# canny edge detector to detect multiple edges in a image

# steps
# 1. noise reduction 2. Gradient Calculation
# 3. Non - Maximum Suppression 4. Double Threshold
# 5. Edge Tracking by Hysteresis

canny = cv2.Canny(img,100, 200)

lap = cv2.Laplacian(img,cv2.CV_64F, ksize=3)

lap = np.uint8(np.absolute(lap))

#sobel gradient dx = 1 dy = 0 => dx is change along x , dy => change along y
sobelX = cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY = cv2.Sobel(img,cv2.CV_64F,0,1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX,sobelY)

titles = ['image','canny','Laplacian','sobelX','sobelY','sobelCombined']
images = [img,canny,lap,sobelX,sobelY,sobelCombined]


for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()