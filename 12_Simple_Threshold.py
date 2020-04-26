import cv2
import numpy as np

while(1):

    img = cv2.imread('./data/gradient.png',0)

    _, th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
    _, th2 = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
    _, th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC) # pixel value remain as 127 from first 127
    
    #threshold less that 127 will be assigned to zero
    _, th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
    _, th5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
    cv2.imshow('image',img)
    cv2.imshow('thres',th1)
    cv2.imshow('thres1',th2)
    cv2.imshow('thres2',th3)
    cv2.imshow('thres3',th4)
    cv2.imshow('thres4',th5)


    k = cv2.waitKey(1)

    if k == 27:
        break

cv2.destroyAllWindows()

