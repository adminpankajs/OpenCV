import cv2

image = cv2.imread('sample.jpg',cv2.IMREAD_UNCHANGED)

cv2.imshow('Image Name',image)

cv2.waitKey()