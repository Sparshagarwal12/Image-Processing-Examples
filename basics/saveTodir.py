import cv2

img = cv2.imread("img.jpeg",0)
# newImg = cv2.resize(img,(0,0),fx = 0.75,fy = 0.75)

# Other Method
newImg = cv2.resize(img,(500,300))
cv2.imshow("Original Image",img)
cv2.imshow("Resized Image",newImg)
output = "/home/sanchit/MyProjects/imageProcessing/basics/output/san.jpg"
cv2.imwrite(output,img)
cv2.waitKey(0)
