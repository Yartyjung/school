# Sobel Method
import cv2 as cv
import numpy as np

img = cv.imread("road.jpg")
kernel = np.ones((3,3),np.uint8)

upper_yellow = np.array([255,255,255])
lower_yellow = np.array([130,190,240])

result= cv.inRange(img,lower_yellow,upper_yellow)
open = cv.morphologyEx(result,cv.MORPH_CLOSE,kernel,1)
open = cv.morphologyEx(open,cv.MORPH_OPEN,kernel,1)


canny =cv.Canny(open,150,200 ,apertureSize=3)
lines = cv.HoughLinesP(canny,1,np.pi/180,70,minLineLength=300,maxLineGap=250)
for line in lines :
    x1,y1,x2,y2 = line[0]
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()