# Sobel Method
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("coins.jpg", 0)

# sobel = cv.Sobel(1,2,3,4)
# 1 คือ รูปภาพ
# 2 คือ ชนิดตัวแปรใน Array (กำหนดค่าเป็น -1 เพื่อให้อ้างอิงกับ Array ของภาพ)
# 3 คือ ตัวแกรเดียนแนวแกน X
# 4 คือ ตัวกรองในแนวแกน Y
sobelX = cv.Sobel(img, -1, 1, 0)
sobelY = cv.Sobel(img, -1, 0, 1)
sobelXY = cv.bitwise_or(sobelX, sobelY)
lapa = cv.Laplacian(img,-1) #add blur or brighnes for better output
canny  =cv.Canny(img,50,200)

images = [img, sobelX, sobelY, sobelXY, lapa, canny]
titles = ["Original", "SobelX", "SobelY", "SobelXY", "Laplacian", "Canny"]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
