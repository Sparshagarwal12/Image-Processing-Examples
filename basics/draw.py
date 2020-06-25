import cv2
import numpy as np

img1 = np.zeros((512,512,3),np.uint8)
#draw line 
cv2.line(img1,(86,86),(86,150),(255,0,0),1)
#draw rectangle
cv2.rectangle(img1,(40,60),(80,70),(255,0,0),1)
#draw circle
cv2.circle(img1,(100,100),50,(0,255,0),1)
#draw ellipse
cv2.ellipse(img1,(95,90),(50,20),0,0,360,(255,0,0),1)
#draw ploylines
points = np.array([[80,2],[125,0],[179,0],[230,5],[30,50]],np.int32)
points = points.reshape((-1,1,2))
cv2.polylines(img1,[points],True,(0,255,255))

#write Text
text = "Hello Sanchit"
cv2.putText(img1,text,(10,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255))
cv2.imshow("Numpy",img1)
cv2.waitKey(0)