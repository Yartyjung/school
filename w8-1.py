import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("coin.jpg")

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, result0 = cv.threshold(gray_img, 128, 255, cv.THRESH_BINARY)

result1 = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 3)

result2 = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 9, 3)

_, result3 = cv.threshold(gray_img, 128, 255, cv.THRESH_BINARY_INV)

_, result4 = cv.threshold(gray_img, 128, 255, cv.THRESH_TRUNC)

_, result5 = cv.threshold(gray_img, 128, 255, cv.THRESH_TOZERO)

_, result6 = cv.threshold(gray_img, 128, 255, cv.THRESH_TOZERO_INV)

kernel = np.ones((5,5),np.uint8)
kernel2 = np.ones((5,5),np.uint8)/5

mo1 = cv.erode(gray_img,kernel,5)
mo2 = cv.dilate(gray_img,kernel,5)
mo3 = cv.morphologyEx(gray_img,cv.MORPH_OPEN,kernel,5) 
mo4 = cv.morphologyEx(gray_img,cv.MORPH_CLOSE,kernel,5) 
mo5 = cv.morphologyEx(gray_img,cv.MORPH_GRADIENT,kernel,5) 

co1 = cv.filter2D(mo4,-1,kernel2)
co2 = cv.blur(mo4,(5,5))
co3 = cv.medianBlur(mo4,5)
co4 = cv.GaussianBlur(mo4,(5,5),10)

image_processing_steps = [
    "original image",
    "grayscale",
    "binary",
    "binary_inv",
    "thresh_trunc",
    "tozero",
    "tozero_inv",
    "adaptive_mean",
    "adaptive_gaussian",
    "erosion",
    "dilation",
    "opening",
    "closing",
    "gradient",
    "filter2D",
    "Mean filter",
    "Median filter",
    "gaussian_filter"
]
list_result = [
    img,
    gray_img,
    result0,
    result3,
    result4,
    result5,
    result6,
    result1,
    result2,
    mo1,
    mo2,
    mo3,
    mo4,
    mo5,
    co1,
    co2,
    co3,
    co4
]
for i in range(18):
    plt.subplot(3,6,i+1,title=image_processing_steps[i])
    plt.imshow(list_result[i],cmap='gray')
plt.show()