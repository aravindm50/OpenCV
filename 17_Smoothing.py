import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('./data/baboon.jpg')
img  = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#homogenous kernel formula
kernel = np.ones((5,5),np.float32)/25

# can be used to blur an image
dst = cv2.filter2D(img,-1,kernel)

blur = cv2.blur(img,(5,5))

# Gaussian filter has higher weights at the center and decreases towards border
# Gaussian filter is used to remove high frequency noise
gblur = cv2.GaussianBlur(img, (5,5),0)

#median filter to remove small dots in the image
median = cv2.medianBlur(img,5)

#bilateral filter to preserve edges. sometimes image can appear like cartoons -staircase effect
# gradient reversal effect- intoduction of false edges
bilateral = cv2.bilateralFilter(img,9,75,75)

# low pass filter can be used to blur the image
# high pass filter can be used to find the edges



titles = ['image','2d convolution','blur','gaussian blur','median blur', 'bilateral']
images = [img,dst,blur,gblur, median, bilateral]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

