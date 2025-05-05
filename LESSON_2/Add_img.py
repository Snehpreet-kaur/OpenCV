import cv2
import numpy as np

image1 = cv2.imread('lion1.jpg')
image2 = cv2.imread('lion2.jpg')

Ws = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)

cv2.imshow('Weighted Image', Ws)

cv2.waitKey(0)
cv2.destroyAllWindows()

