import cv2
from matplotlib import pyplot as plt

while(1):

    img = cv2.imread('./data/lena.jpg',-1)

    cv2.imshow('image',img)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.show()

    k = cv2.waitKey(0)
    if k== 27:
        break

cv2.destroyAllWindows()
