import cv2 as cv
import numpy as np
#640 x 480
vid = cv.VideoCapture(0)
kernel = np.ones((7,7),np.uint8)
img = np.zeros([480,640,3],dtype="uint8")
old = None

while True :
    _,frame = vid.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # _, binary = cv.threshold(gray_frame, 80, 255, cv.THRESH_BINARY_INV)
    # closed = cv.morphologyEx(binary,cv.MORPH_CLOSE,kernel,5) 
    # cleaned = cv.morphologyEx(closed,cv.MORPH_OPEN,kernel,5) 
    # contours,hierarchys = cv.findContours(cleaned,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    # mod_frame = cv.drawContours(frame,contours,-1,(0,255,0),2)
    # cv.imshow("frame",cleaned)
    # cv.imshow("frame2",gray_frame)
    # cv.imshow("frame3",mod_frame)
    try :
        before
    except NameError :
        before = gray_frame.copy()
    frame = cv.absdiff(gray_frame,before)
    cv.imshow("nigga",frame)
    before = gray_frame.copy()
    if cv.waitKey(1) & 0xFF == ord('0'): 
        break

cv.destroyAllWindows()
vid.release()
