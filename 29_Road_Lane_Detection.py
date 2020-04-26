import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./data/lane3.jpeg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(image.shape)
height = image.shape[0]
width = image.shape[1]

region_of_interest = [(0,height),(width/2,height/2),(width,height)]

def roi(img,vertices):
    mask = np.zeros_like(img)
    #channel_count= img.shape[2]
    match_mask_color = 255#*channel_count
    cv2.fillPoly(mask,vertices,match_mask_color)
    masked_image = cv2.bitwise_and(img,mask)
    return masked_image

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny_image = cv2.Canny(gray_image, 100,200)
cropped_image = roi(canny_image, np.array([region_of_interest],np.int32))

lines = cv2.HoughLinesP(cropped_image,1,np.pi/60,
                        threshold=160,
                        lines=np.array([]),
                        minLineLength=40,
                        maxLineGap=25)

def draw_lin(img, lines):
    copy_img = np.copy(img)
    line_image = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_image, (x1,y1),(x2,y2),(0,255,0),3)

    img = cv2.addWeighted(img,0.8, line_image, 1, 0.0)
    return  img

image_with_lines = draw_lin(image,lines)
plt.imshow(image_with_lines)
plt.show()