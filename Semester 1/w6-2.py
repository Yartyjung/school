import cv2 as cv
import numpy as np

rectangle = np.zeros((480,640,3),dtype="uint8")
rectangle[:] = [255,255,255]
cv.rectangle(rectangle,(0,0),(640,480),(0,0,255),-1)

circle = np.zeros((480,640,3),dtype="uint8")
circle[:] = [0,0,0]
cv.circle(circle,(320,240),240,(255,255,255),-1)

aim = cv.bitwise_or(rectangle,circle)

vid = cv.VideoCapture(0)
while True:
    ret,frame = vid.read()
    hsvFrame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    yellow_max = np.array([50,240,255],dtype="uint8")
    yellow_min = np.array([10,40,120],dtype="uint8")
    yellow_mask = cv.inRange(hsvFrame,yellow_min,yellow_max)

    aim_frame = cv.bitwise_and(frame,circle,mask=yellow_mask)

    cv.imshow("original",frame)
    cv.imshow("masked",aim_frame)

    if cv.waitKey(1) == 27:
        print(frame.shape) #640 x 480
        cv.destroyAllWindows()
        break