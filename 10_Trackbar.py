import cv2
import numpy as np

def nothing(x):
    print(x)

#img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')

#cv2.createTrackbar('B','image',0,255,nothing)
#cv2.createTrackbar('G','image',0,255,nothing)
#cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('CP','image',10,400,nothing)

switch = 'color / gray'
cv2.createTrackbar(switch,'image',0,1,nothing)

while(1):
    img = cv2.imread('./data/lena.jpg')
    pos = cv2.getTrackbarPos('CP','image')
    k = cv2.waitKey(1) & 0xFF
    if k == 27 :
        break

    #b = cv2.getT rackbarPos('B','image')
    #g = cv2.getTrackbarPos('G','image')
    
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        pass
    else:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    img = cv2.imshow('image',img)

#cv2.waitKey(10000)
cv2.destroyAllWindows()