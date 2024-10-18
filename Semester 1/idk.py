import cv2 as cv

vid_capture = cv.VideoCapture(0)


while vid_capture.isOpened():
    ret, frame1 = vid_capture.read()
    ret, frame2 = vid_capture.read()
    if ret:
        graying = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)
        graying2 = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(graying, (5, 5), 0) 
        thresh, result = cv.threshold(blur, 50, 255, cv.THRESH_BINARY)
        dilation = cv.dilate(result, None, iterations=3)
        motiondiff = cv.absdiff(graying2, result)
        cv.imshow('Frame', motiondiff)
        frame1 = frame2
        ret, frame2 = vid_capture.read()
        key = cv.waitKey(1)
        if key == ord('q'):
            break
    else:
        print("Error: Failed to capture image.")
        break

vid_capture.release()
cv.destroyAllWindows()