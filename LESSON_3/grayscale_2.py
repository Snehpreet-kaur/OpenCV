# Using averaging of pixels method to grayscale the image
# Without using the library to grayscale the image
import cv2

img = cv2.imread('pika.png')
(row, col) = img.shape[0:2]

for i in range(row):
	for j in range(col):
		# Find the average of the BGR pixel values
		img[i, j] = sum(img[i, j]) * 0.33

cv2.imshow('Grayscale Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()