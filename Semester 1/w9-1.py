import cv2 as cv 
import numpy as np

img = cv.imread("resize_coins.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
kernel = np.ones((10,10),np.uint8)



_, binary = cv.threshold(gray_img, 128, 255, cv.THRESH_BINARY_INV)
closed = cv.morphologyEx(binary,cv.MORPH_CLOSE,kernel,10) 
blur = cv.GaussianBlur(closed,(5,5),10)

contour_line,hierarchy = cv.findContours(blur,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
draw_contour = cv.drawContours(img,contour_line,-1,(0,255,255),3)


cv.imshow("image",closed)
cv.waitKey(0)
cv.destroyAllWindows()