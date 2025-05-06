#### Draw some text on the image

# Python program to explain cv2.putText() method
	
# importing cv2
import cv2
image = cv2.imread("lion1.jpg")

# font
font = cv2.FONT_HERSHEY_SIMPLEX
# orgin
org = (50, 50)
# fontScale
fontScale = 1
# Blue color in BGR
color = (255, 0, 0)
# Line thickness of 2 px
thickness = 2
# Using cv2.putText() method
image = cv2.putText(image, 'OpenCV', org, font, fontScale, color, thickness, cv2.LINE_AA)

cv2.imshow("OUTPUT", image)
cv2.waitKey(0)
cv2.destroyAllWindows()