import cv2

img=cv2.imread("pika.png",1)
cv2.imshow("Original Image",img)

resized=cv2.resize(img,(300,300))
cv2.imshow("reducedImage", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
