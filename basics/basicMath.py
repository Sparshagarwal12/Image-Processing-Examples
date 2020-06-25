import cv2

img = cv2.imread("img.jpeg")

#return numpy array
print(img)

#retrun the height, width, number of color channels
print(img.shape)

#return number of dimension of image
print(img.ndim)

#return size of image
print(img.size)