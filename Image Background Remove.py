import cv2
import numpy as np

img = cv2.imread('view2.jpeg')

scale_percent = 20 
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
print('Resized Dimensions : ',resized.shape)

hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv, (0, 0, 200), (179, 100, 255))

white = cv2.bitwise_and(resized,resized, mask= mask)

cv2.imshow('Image', white)
cv2.waitKey(0)

#(0, 0, 200), (179, 100, 255)