#### Draw a line on the image

# importing cv2 
import cv2 
image = cv2.imread("pika.png")

# Start coordinate, here (0, 0) represents the top left corner of image
start_point = (0, 0)
# End coordinate, here (250, 250) represents the bottom right corner of image
end_point = (250, 250)
# Green color in BGR
color = (0, 255, 0)
# Line thickness of 9 px
thickness = 9
  
# Using cv2.line() method
# Draw a diagonal green line with thickness of 9 px
image = cv2.line(image, start_point, end_point, color, thickness)
  

cv2.imshow("Image", image) 
cv2.waitKey(0)
cv2.destroyAllWindows()