import cv2
import numpy as np
# cap = cv2.VideoCapture(0)

frame = cv2.imread("lane tracking//img.png")
roi = frame[130:400,5:635]
drawing_pts = np.array([[[0, 130],[0, 400],[640, 400],[640, 130]]], np.int32)
cv2.polylines(frame, [drawing_pts],True, (0,255,),3)
cv2.imshow("frame",frame)
cv2.imshow("img",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()