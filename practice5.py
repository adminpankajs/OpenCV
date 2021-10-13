import cv2

image = cv2.imread('test.jpg')
imageRL = cv2.resize(image,None,fx=0.5,fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow('img',imageRL)
imageRL = cv2.resize(image,None,fx=0.5,fy=0.5, interpolation=cv2.INTER_CUBIC)
cv2.imshow('img',imageRL)
cv2.waitKey()
