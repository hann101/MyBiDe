import cv2
path = './test.png'

image = cv2.imread(path)
cv2.imshow("original", image)
cv2.waitKey(0)