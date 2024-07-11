import cv2 as cv
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
img_id = 0
id = 1


def draw_boundary(img, clf):
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detect = face_cascade.detectMultiScale(gray_img, 1.1, 5)
    xywh = []
    for (x, y, w, h) in face_detect:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)
        cv.rectangle(img, (x, y - 50), (x + w, y), (0, 0, 255), -1)
        id, con = clf.predict(gray_img[y:y + h, x:x + w])
        if con <= 50:
            cv.putText(img, "yartyjung", (x + 10, y - 10), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
        else:
            cv.putText(img, "unknown nigga", (x + 10, y - 10), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
            show_con = "{0}%".format(round(100 - con))
            cv.rectangle(img, (x + 10, y + h + 10), (x + w, y + h + 50), (255, 0, 255), -1)
            cv.putText(img, show_con, (x + 10, y + h + 40), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        xywh = [x, y, w, h]
    return img, xywh

def detect(img, img_id, clf):
    img, xywh = draw_boundary(img, clf)
    if len(xywh) == 4:
        result = img[xywh[1]:xywh[1] + xywh[3], xywh[0]:xywh[0] + xywh[2]]
    return img

clf = cv.face.LBPHFaceRecognizer_create()
clf.read("year.xml")

cap = cv.VideoCapture(0)

while True:
    check, frame = cap.read()
    frame = detect(frame,img_id,clf)
    cv.imshow("output_cam",frame)
    img_id += 1
    if cv.waitKey(40)& 0xff == ord("q"):
        break

cap.release()
cv.destroyAllWindows()

