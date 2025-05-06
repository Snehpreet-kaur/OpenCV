##### Rotating an image
import cv2

img = cv2.imread('lion2.jpg')
(rows, cols) = img.shape[:2]

# getRotationMatrix2D creates a matrix needed for transformation.
# We want matrix for rotation w.r.t center to 45 degree without scaling.
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
res = cv2.warpAffine(img, M, (cols, rows))

cv2.imwrite('result.jpg', res)