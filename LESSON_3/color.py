##### Convert the image from one color frame to another
# Convert an image from RGB to HSV 

# Python program to explain cv2.cvtColor() method

import cv2

image = cv2.imread('pika.png')
hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV )

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()