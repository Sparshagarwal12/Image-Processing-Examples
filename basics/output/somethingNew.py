import numpy as np
import cv2


windowName = 'Drawing'
img = np.zeros([1012,1012,3],np.uint8)
cv2.namedWindow(windowName)

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),40,(0,255,0),2)
    if event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(img,(x,y),40,(0,0,255),2)

cv2.setMouseCallback(windowName,draw_circle)

def main():
    while(True):
        cv2.imshow(windowName,img)
        if cv2.waitKey(27)==27:
            break
    
    cv2.destroyAllWindow()

if __name__ =='__main__':
    main()
