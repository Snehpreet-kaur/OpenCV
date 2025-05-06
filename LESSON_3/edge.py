##### Edge Detection in an image
import cv2
img = cv2.imread('pika.png')
# We are using the Canny Edge Detection Algorithm here
# No need to dive deep into explanation over here
edges = cv2.Canny(img, 100, 200)

cv2.imwrite('result.jpg', edges)
