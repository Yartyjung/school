import cv2 as cv
import numpy as np
 
vid_capture = cv.VideoCapture(0)
 
circle = np.zeros((300,300,3),dtype="uint8")
circle[:] = [255,255,255]
cv.circle(circle,(150,150),150,(0,0,255),-1)
cv.imshow("Circle",circle)
 
while(vid_capture.isOpened()):
    ret, frame = vid_capture.read()
    if ret ==True:
        upper_yellow = np.array([40,240,240])
        lower_yellow = np.array([17,10,10])
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        mask = cv.inRange(hsv,lower_yellow,upper_yellow)
        result = cv.bitwise_and(frame,frame,mask=mask)
        cv.imshow("ori",frame)
        cv.imshow("mask",mask)
        cv.imshow("result",result)
        key = cv.waitKey(33)
        if key == ord('q'):
            break
    else:
        break
 
vid_capture.release()
cv.destroyAllWindows()