import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./data/lena.jpg')
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

layer = img.copy()

gp =[layer]

#laplacian pyramid is diff between that level gaussian pyramid and expanded
# version of upper level of Gaussian Pyramid

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i),layer)

layer = gp[5]
cv2.imshow('last level',layer)
lp = [layer]

for i in range(5,0,-1):
    gaussian_ext = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussian_ext)
    cv2.imshow(str(i),laplacian)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# reduce resolution
'''lr = cv2.pyrDown(img)

# increase resolution
ir = cv2.pyrUp(img)

titles=['img','lr','ir']
images = [img,lr,ir]

for i in range(3):
    #plt.subplot(1,3,i+1)
    plt.figure()
    plt.imshow(images[i],'gray')
    plt.title(titles[i])

    plt.show()'''