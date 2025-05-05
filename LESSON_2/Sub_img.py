import cv2

image1=cv2.imread('lion1.jpg')
image2=cv2.imread('lion2.jpg')

sub=cv2.subtract(image1,image2)

cv2.imshow('Subtracted Image',sub)

cv2.waitKey(0)
cv2.destroyAllWindows()