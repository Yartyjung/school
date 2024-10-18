import cv2 as cv
import numpy as np

rectangle = np.zeros((300,300,3),dtype="uint8")
rectangle[:] = [255,255,255]
cv.rectangle(rectangle,(25,25),(275,275),(0,0,255),-1)
# cv.imshow("Rectangle",rectangle)

circle = np.zeros((300,300,3),dtype="uint8")
circle[:] = [255,255,255]
cv.circle(circle,(150,150),150,(0,0,255),-1)
# cv.imshow("Circle",circle)

bitwise_and = cv.bitwise_and(circle,rectangle)
cv.imshow("and",bitwise_and)

# bitwise_not = cv.bitwise_not(circle,rectangle)
# cv.imshow("not",bitwise_not) # nigga it has a bug

bitwise_or = cv.bitwise_or(circle,rectangle)
cv.imshow("or",bitwise_or)

bitwise_xor = cv.bitwise_xor(circle,rectangle)
cv.imshow("xor",bitwise_xor)

cv.waitKey(0)
cv.destroyAllWindows()