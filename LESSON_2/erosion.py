#corners are trimmed in erosion
import cv2
import numpy as np

image = cv2.imread("pika.png",1)

#kernel is used for erosion as an input
kernel=np.ones((5,5),np.uint8)

image=cv2.erode(image,kernel)
cv2.imshow("Eroded Image",image)

cv2.waitKey(0)
cv2.destroyAllWindows()