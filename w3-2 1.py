import cv2 as cv
import numpy as np

vid = cv.VideoCapture(0) #(480, 640, 3)
while(True): 
    ret, frame = vid.read() 
    y,x,_ = np.shape(frame)
    cv.circle(frame,(int(x/2),int(y/2)),50,(50,255,0),5)
    cv.rectangle(frame,(0,0),(x,y),(220,140,0),20)
    cv.line(frame,(0,0),(x,y),(0,20,255),7)
    cv.putText(frame,"Live Video",(20,30),fontFace=1,fontScale=1,color=(0,0,0),thickness=2)

    cv.imshow('frame', frame) 
      

    if cv.waitKey(1) & 0xFF == ord('0'): 
        break
  

vid.release() 
cv.destroyAllWindows() 