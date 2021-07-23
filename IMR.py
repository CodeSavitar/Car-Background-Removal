import cv2
import numpy as np

def get_masked_image(resized):

    hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0, 0, 200), (179, 100, 255))
    white = cv2.bitwise_and(resized, resized, mask = mask)
    return white, mask
