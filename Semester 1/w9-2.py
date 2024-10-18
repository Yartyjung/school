import cv2 as cv
import numpy as np

vid = cv.VideoCapture("coins_vid.mp4")
kernel = np.ones((7,7),np.uint8) 

while True :
    new_contour = []
    counter = 0
    ret,frame = vid.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    _, binary = cv.threshold(gray_frame, 160, 255, cv.THRESH_BINARY_INV)
    closed = cv.morphologyEx(binary,cv.MORPH_CLOSE,kernel,5) 
    cleaned = cv.morphologyEx(closed,cv.MORPH_OPEN,kernel,5) 
    contours,hierarchys = cv.findContours(cleaned,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for index,contour in enumerate(contours) :
        area = cv.contourArea(contour)
        if area < 5000 and area >= 1500 :
            if  area < 3000 and area >= 2000:
               counter += 1
            elif area >= 3050 and area < 3550:
                counter += 5
            elif area >= 3550 and area < 5000:
                counter += 10
            new_contour.append(contour)
    mod_frame = cv.drawContours(frame,new_contour,-1,(0,255,0),2)
    mod_frame = cv.putText(mod_frame,f"coin value : {counter}",(10,50),fontFace=1,fontScale=3,color=(0,0,255),thickness=2)
    cv.imshow("frame",mod_frame)
    if cv.waitKey(1) & 0xFF == ord('0'): 
        break

cv.destroyAllWindows()
vid.release()