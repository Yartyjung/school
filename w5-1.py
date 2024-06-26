import cv2 as cv

vid = cv.VideoCapture(0)
while True:
    ret,frame = vid.read()
    pic = frame.copy()
    frame = cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
    harr_face = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
    harr_eye = cv.CascadeClassifier("haarcascade_eye.xml")
    pos1 = harr_face.detectMultiScale(frame)
    pos2 = harr_eye.detectMultiScale(frame)
    for (x,y,w,h) in pos1 :
        cv.rectangle(pic,(x,y),(x+w,y+h),(244,10,252),3)
    for (x,y,w,h) in pos2 :
        cv.rectangle(pic,(x,y),(x+w,y+h),(252,239,2),3)
    cv.imshow("img",pic)
    if cv.waitKey(1) & 0xFF == ord('0'): 
        break

vid.release()
cv.destroyAllWindows()