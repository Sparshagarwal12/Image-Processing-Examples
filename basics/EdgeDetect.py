import cv2

img = cv2.imread("img.jpeg")

edge_image = cv2.Canny(img,100,200)

cv2.imshow("Detect Edge",edge_image)
# cv2.imshow("Detect Edge",img)


cv2.waitKey(0)