import cv2
import numpy as np
from IMR import get_masked_image

img = cv2.imread('view2.jpeg')

scale_percent = 20 
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
# print('Resized Dimensions : ',resized.shape)

white_img, masked_img = get_masked_image(resized)

masked_image = np.copy(resized)
masked_image[masked_img == 0] = [0, 0, 0]

background = cv2.imread('Background.jpg')
background = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)
crop_background = background[0:604, 0:806]

crop_background[masked_img != 0] = [0, 0, 0]

complete_image = white_img + crop_background

cv2.imshow('Image',complete_image)
cv2.waitKey(0)