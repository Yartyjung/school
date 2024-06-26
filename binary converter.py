import cv2 as cv
import numpy as np
img = cv.imread("custom-nike-air-force-1-mid-by-you-shoes.png",0)
x,y = np.shape(img)
print(img)
for i in range(x):
    for j in range(y):
        if img[i][j] >= 200 :
            img[i][j] = 0
        else : img[i][j] = 255

cv.imshow("wow",img)
cv.waitKey(0)