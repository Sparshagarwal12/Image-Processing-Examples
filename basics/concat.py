
# Important Note:

# Use cv2.vconcat(), cv2.hconcat() to concatenate (combine) images vertically and horizontally
# Images with different sizes need to be resized beforehand. Errors will occur if the width or height is not aligned.
# numpy.tile() is convenient when arranging the same image repeatedly.

import cv2

img1 = cv2.imread('img.jpeg')
img2 = cv2.imread('img.jpeg')

v_cat = cv2.vconcat([img1,img2])
h_cat = cv2.hconcat([img1,img2])

cv2.imshow('Vertical Concatination',v_cat)
cv2.imshow('Horizontal Concatination',h_cat)
cv2.waitKey(0)
cv2.destroyAllWindow()
