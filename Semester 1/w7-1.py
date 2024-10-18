import cv2 as cv

cap = cv.VideoCapture(0)
cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

def capture_image(frame,id,index):
    cv.imwrite(f"data/{id}-{index}.jpg",frame)

def boundary(frame):
    img = frame.copy()
    g_frame = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face = cascade.detectMultiScale(g_frame,1.1,5)
    print("detect")
    for (x,y,w,h) in face :
        xywh = [x,y,w,h]
        print("return")
        return  xywh
  
def cs(frame,index,img_id):
    xywh = boundary(frame) 
    print("pass")   
    if len(xywh) == 4 :
        cropped = frame[xywh[1]:xywh[1]+xywh[3],xywh[0]:xywh[0]+xywh[2]]
        capture_image(cropped,index,img_id)
        print("saved" + str(img_id))
        img_id += 1
        return cropped


img_id = 1
#1)year 2)tawan 3)nam 4)dd 5)kla 6) preme
while True:
    ret,frame = cap.read()
    cs(frame,6,img_id)
    img_id += 1
    cv.imshow("yay",frame)
    if cv.waitKey(40)& 0xff == ord("q"):
        break

cap.release()
cv.destroyAllWindows()