import cv2 as cv

vid_capture = cv.VideoCapture("cars.mp4")


while vid_capture.isOpened():
    ret, frame1 = vid_capture.read()
    ret, frame2 = vid_capture.read()
    if ret:
        motiondiff = cv.absdiff(frame1, frame2)
        graying = cv.cvtColor(motiondiff, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(graying, (5, 5), 0) 
        thresh, result = cv.threshold(blur, 50, 255, cv.THRESH_BINARY)
        dilation = cv.dilate(result, None, iterations=3)
        contours, hierarchy = cv.findContours(dilation, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        # cv.drawContours(frame1, contours, -1, (255, 0, 0), 2)
        for contour in contours:
            (x, y, w, h) = cv.boundingRect(contour)
            if cv.contourArea(contour) < 1700:
                continue
            cv.rectangle(frame1, (0,0), (640,480), (0, 0, 255), 10)
        cv.imshow('Frame', frame1)
        frame1 = frame2
        ret, frame2 = vid_capture.read()
        key = cv.waitKey(33)
        if key == ord('q'):
            break
    else:
        print("Error: Failed to capture image.")
        break

vid_capture.release()
cv.destroyAllWindows()