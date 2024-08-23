import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math

def canny(img):
    gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    blur = cv.GaussianBlur(gray,(5,5), 0)
    canny = cv.Canny(blur,50,150)
    return canny
def region_of_interest(img):
    height = img.shape[0]
    polygons = np.array([[(200, height), (1100, height), (550, 250)]], dtype=np.int32)
    mask = np.zeros_like(img)
    cv.fillPoly(mask, polygons, 255)
    masked_img = cv.bitwise_and(img, mask)
    return masked_img
def line_displsy(img,lines):
    lins_img = np.zeros_like(img)
    if lines is not None :
        for line in lines:
            x1 , y1, x2, y2 = line.reshape(4)
            cv.line(lins_img, (x1,y1),(x2,y2),(255,0,0),10)
    return lins_img
def make_coordinates(img,line_parameters):
    slop,intercept = line_parameters
    y1 = img.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1-intercept)/slop)
    x2 = int((y2-intercept)/slop)
    return np.array([x1,y1,x2,y2])
def averaged_slop_intercept(img,lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1 , y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1,x2),(y1,y2),1)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            left_fit.append((slope,intercept))
        else:
            right_fit.append((slope,intercept))
    left_fit_average = np.average(left_fit,axis=0)
    right_fit_average = np.average(right_fit,axis=0)
    left_line = make_coordinates(img,left_fit_average)
    right_line = make_coordinates(img,right_fit_average)
    return np.array([left_line,right_line])

def get_steering_angle(img,lane_line):
    height,width,_= img.shape
    if len(lane_line)== 2 :
        _,_,left_x2,_ = lane_line[0]
        _,_,right_x2,_ = lane_line[1]
        mid = int(width/2)
        x_offset = (left_x2+right_x2)/2 -mid
        y_offset = int(height/2)
    elif len(lane_line) == 1:
        x1,_,x2,_ = lane_line[0]
        x_offset = x2-x1
        y_offset = int(height/2)
    elif len(lane_line)==0:
        x_offset = 0
        y_offset = int(height/2)
    
    angle_to_mid_radian = math.atan(x_offset/y_offset)
    angle_to_mid_deg = int(angle_to_mid_radian*180/np.pi)
    steering_angle = angle_to_mid_deg

    return steering_angle


vid= cv.VideoCapture(0)
# vid= cv.VideoCapture('C:\\personal file\\github\\school\\lane tracking\\drive.mp4')

while True :
    _, img=  vid.read()
    lane_img = np.copy(img)
    canny_img = canny(lane_img)
    roi_img = region_of_interest(canny_img)
    lines = cv.HoughLinesP(roi_img,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=50)
    averaged_line = averaged_slop_intercept(lane_img,lines)
    line_img = line_displsy(lane_img,averaged_line)
    combo = cv.addWeighted(lane_img,0.8,line_img,1,1)
    angle = get_steering_angle(img,averaged_line)
    print(angle)
    # cv.imshow('lane',combo)
    # cv.imshow('canny',canny_img)
    cv.imshow('roi',roi_img)
    cv.imread
    key = cv.waitKey(33)
    if key == ord('q'):
        break