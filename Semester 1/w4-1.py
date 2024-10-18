import cv2 as cv
import numpy as np

img = np.zeros([600,600,3],dtype="uint8")
on_click = []
on_release = []
on_click_state = False
was_drawn = False
Blue,Green,Red = None,None,None
def click_event(event,x,y,flags,param):
    global bg ,on_click, on_click_state, on_release,was_drawn ,img,Blue,Green,Red
    bg = img
    if event == cv.EVENT_LBUTTONDOWN:
        on_click = [x,y]
        on_click_state = True
        Red,Blue,Green = np.random.randint(255),np.random.randint(255),np.random.randint(255)
        print(on_click,"onclick")
        cv.imshow("Img",bg)
    elif event == cv.EVENT_MOUSEMOVE:
        current_pos = [x,y]
        print(current_pos)
        dyn = img.copy()
        if on_click_state == True:
            cv.rectangle(dyn,(on_click[0],on_click[1]),(current_pos[0],current_pos[1]),(Blue,Green,Red),2)
            was_drawn = True
            cv.imshow("Img",dyn)
            print("drawn")
    elif event == cv.EVENT_LBUTTONUP:
        on_release = [x,y]
        print(on_release,"onrele")
        on_click_state = False
        if was_drawn == True:
            cv.rectangle(img,(on_click[0],on_click[1]),(on_release[0],on_release[1]),(Blue,Green,Red),2)
            cv.imshow("Img",img)
            was_drawn = False
            
cv.imshow("Img",img)
cv.setMouseCallback("Img",click_event)
cv.waitKey(0)
