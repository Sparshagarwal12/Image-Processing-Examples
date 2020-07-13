import cv2

# Condition of Flipping

# 0, for flipping the image around the x-axis (vertical flipping);
# > 0 for flipping around the y-axis (horizontal flipping);
# < 0 for flipping around both axes.


img = cv2.imread('img.jpeg')

flip = cv2.flip(img,0)
flip2 = cv2.flip(img,-1)

cv2.imshow('Original Image',img)
cv2.imshow('Flip Vertical',flip2)
cv2.imshow('Flipped X-axis',flip)

cv2.waitKey(0)
cv2.destroyAllWindow()