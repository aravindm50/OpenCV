import cv2
import numpy as np

#img=cv2.imread('./data/lena.jpg')

img = np.zeros([512,512,3],np.uint8)

img = cv2.line(img,(0,0),(255,255),(255,0,0),5) # point (0,0) to point (255,255) line. Colot Blue in BGR (255,0,0)

img = cv2.line(img,(0,0),(255,255),(255,0,0),5) # point (0,0) to point (255,255) line. Colot Blue in BGR (255,0,0)
img = cv2.arrowedLine(img,(640,480),(255,255),(255,0,0),5) # point (0,0) to point (255,255) line. Colot Blue in BGR (255,0,0)

img = cv2.rectangle(img,(0,0),(320,240),(0,0,0),-1) # -1 will cause the color tobe filled

img = cv2.circle(img, (320,240),20,(255,255,255),-1)

font = cv2.FONT_HERSHEY_TRIPLEX
img = cv2.putText(img,"this is lena's img",(10,500),font,2,(0,255,0),10,cv2.LINE_AA)
cv2.imshow('lena.jpg',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
