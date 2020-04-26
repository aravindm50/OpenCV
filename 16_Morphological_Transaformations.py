import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('./data/smarties.png',cv2.IMREAD_GRAYSCALE)

_,mask = cv2.threshold(img, 220, 255,cv2.THRESH_BINARY_INV)

kernel = np.ones([2,2], np.uint8)

dilation = cv2.dilate(mask,kernel,iterations=5) # kernel is the mask applied on image where black dots are present

erosion = cv2.erode(mask,kernel,iterations = 2) # more number of iter then more erosion of foreground object

#opening is erosion first followed by dilation
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN,kernel)

#closing is dilation first followed by erosion
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,kernel)

# mg is difference between dilation and erosion of image
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT,kernel)

#th is the difference between image and opening of the image
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT,kernel)


titles = ['image','mask', 'dilation','erosion','opening','closing','mg','th']
images = [img,mask,dilation, erosion,opening,closing,mg,th]

for i in range(8):
    plt.subplot(2,4,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

