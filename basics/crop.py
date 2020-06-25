import cv2

img = cv2.imread("img.jpeg")
height,width = img.shape[0:2]

startRow = int(height*.15)
startCol = int(width*.15)
endRow = int(height*.75)
endCol = int(height*.75)

cropImage = img[startRow:endRow,startCol:endCol]
cv2.imshow('Cropped Image',cropImage)
cv2.imshow('Original Image',img)
cv2.waitKey(0)