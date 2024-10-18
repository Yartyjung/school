import cv2 as cv
import numpy as np

img = np.full((600,600,3),255,dtype="uint8")
cv.rectangle(img,(200,250),(400,350),(220,140,0),-1)
cv.circle(img,(300,300),50,(0,20,255),-1)
cv.line(img,(0,0),(600,600),(50,255,0),7)
cv.putText(img,"OpenCV Homework",(20,580),fontFace=1,fontScale=1,color=(0,0,0),thickness=2)

cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()