import cv2

img = cv2.imread("/home/griffonuser/DS_Practise/Open CV/data/lena.jpg",-1)

cv2.imshow('lena.jpg',img)

k = cv2.waitKey(0)

if k == 27:
    print("Destroying Window")
    cv2.destroyAllWindows()
elif k== ord('s'):
    print("Saving Image")
    cv2.imwrite('/home/griffonuser/DS_Practise/Open CV/data/lena_copy.png',img)
    cv2.destroyAllWindows()