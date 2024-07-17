import cv2 as cv
import time 
cap=cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
img_id=0
id = 1
def draw_boundary(img,clf):
      gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
      face_detect=face_cascade.detectMultiScale(gray_img,1.1,5) 
      xywh = []
      for (x,y,w,h) in face_detect :
            cv.rectangle(img, (x,y), (x+w, y+ h), (0,249,0),5) 
            cv.rectangle(img,(x,y-50),(x+w,y),(0,0,249), -1)
            id, con = clf.predict(gray_img[y:y+h,x:x+w])
            current_time = time.localtime()
            print(id," ",con)
            if con >= 49 and id == 1:
                  print("year",id)
                  cv.putText(img, "year", (x+10, y-10), cv. FONT_HERSHEY_SIMPLEX, 1, (249,249, 249), 3)
                  show_con ="{0}%".format(round(100-con))
                  cv.rectangle(img, (x+10,y+h+10), (x+w,y+h+50), (249,0,249), -1)
                  cv.putText(img, show_con, (x+10,y+h+40), cv.FONT_HERSHEY_SIMPLEX,0.8, (249,249,249), 2) 
                  xywh=[x,y,w,h]
                  cv.imwrite(f"login\\year - {time.strftime("%Y-%m-%d %H-%M-%S", current_time)}.png",img,[cv.IMWRITE_PNG_COMPRESSION, 9])
            elif con >= 49 and id == 2:
                  print("tawan",id)
                  cv.putText(img, "tawan", (x+10, y-10), cv. FONT_HERSHEY_SIMPLEX, 2, (249,249, 249), 3)
                  show_con ="{0}%".format(round(100-con))
                  cv.rectangle(img, (x+10,y+h+10), (x+w,y+h+50), (249,0,249), -1)
                  cv.putText(img, show_con, (x+10,y+h+40), cv.FONT_HERSHEY_SIMPLEX,0.8, (249,249,249), 2) 
                  xywh=[x,y,w,h]
                  cv.imwrite(f"login\\tawan - {time.strftime("%Y-%m-%d %H-%M-%S", current_time)}.png",img,[cv.IMWRITE_PNG_COMPRESSION, 9])
            elif con >= 49 and id == 3:
                  print("nam",id)
                  cv.putText(img, "nam", (x+10, y-10), cv. FONT_HERSHEY_SIMPLEX, 2, (249,249, 249), 3)
                  show_con ="{0}%".format(round(100-con))
                  cv.rectangle(img, (x+10,y+h+10), (x+w,y+h+50), (249,0,249), -1)
                  cv.putText(img, show_con, (x+10,y+h+40), cv.FONT_HERSHEY_SIMPLEX,0.8, (249,249,249), 2) 
                  xywh=[x,y,w,h]
                  cv.imwrite(f"login\\nam - {time.strftime("%Y-%m-%d %H-%M-%S", current_time)}.png",img,[cv.IMWRITE_PNG_COMPRESSION, 9])
            elif con >= 49 and id == 4:
                  print("dd",id)
                  cv.putText(img, "dd", (x+10, y-10), cv. FONT_HERSHEY_SIMPLEX, 2, (249,249, 249), 3)
                  show_con ="{0}%".format(round(100-con))
                  cv.rectangle(img, (x+10,y+h+10), (x+w,y+h+50), (249,0,249), -1)
                  cv.putText(img, show_con, (x+10,y+h+40), cv.FONT_HERSHEY_SIMPLEX,0.8, (249,249,249), 2) 
                  xywh=[x,y,w,h]
                  cv.imwrite(f"login\\dd - {time.strftime("%Y-%m-%d %H-%M-%S", current_time)}.png",img,[cv.IMWRITE_PNG_COMPRESSION, 9])
            elif con >= 49 and id == 5:
                  print("kla",id)
                  cv.putText(img, "kla", (x+10, y-10), cv. FONT_HERSHEY_SIMPLEX, 2, (249,249, 249), 3)
                  show_con ="{0}%".format(round(100-con))
                  cv.rectangle(img, (x+10,y+h+10), (x+w,y+h+50), (249,0,249), -1)
                  cv.putText(img, show_con, (x+10,y+h+40), cv.FONT_HERSHEY_SIMPLEX,0.8, (249,249,249), 2) 
                  xywh=[x,y,w,h]
                  cv.imwrite(f"login\\kla - {time.strftime("%Y-%m-%d %H-%M-%S", current_time)}.png",img,[cv.IMWRITE_PNG_COMPRESSION, 9])
      return img,xywh
def detect(img,img_id,clf) :



      img,xywh=draw_boundary(img, clf) 
      if len(xywh) == 4 :
            result=img[xywh[1]:xywh[1 ]+xywh[3],xywh[0]:xywh[0]+xywh[2]]
      return img

clf=cv.face.LBPHFaceRecognizer_create()
clf.read("classifier.xml")

while (True):
      check, frame=cap.read()
      frame=detect(frame,img_id,clf)
      cv.imshow("output camera",frame)
      img_id +=1
      if cv.waitKey(1) & 0xFF == ord("g"):
            break
cap.release()
cv.destroyAllWindows()