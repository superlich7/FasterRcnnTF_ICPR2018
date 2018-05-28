import numpy as np
import cv2

img_file = 'image_10000/TB1mHxFLXXXXXbjXFXXunYpLFXX.jpg'

img = cv2.imread(img_file)

img_hor_flip = img[:, ::-1, :]
img_ver_flip = img[::-1,:,:]
img_all_flip = img[::-1,::-1,:]

cv2.imwrite('img_hor_flip.jpg',img_hor_flip)
cv2.imwrite('img_ver_flip.jpg',img_ver_flip)
cv2.imwrite('img_all_flip.jpg',img_all_flip)
