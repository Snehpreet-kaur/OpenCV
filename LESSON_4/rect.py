#### Draw a rectangle on the image
 
import cv2 
image = cv2.imread("pika.png")
  
# Start coordinate, here (5, 5) represents the top left corner of rectangle
start_point = (5, 5)
# Ending coordinate, here (220, 220) represents the bottom right corner of rectangle
end_point = (220, 220) 
# Blue color in BGR
color = (255, 0, 0)
# Line thickness of 2 px
thickness = 2
  
# Using cv2.rectangle() method
# Draw a rectangle with blue line borders of thickness of 2 px
image = cv2.rectangle(image, start_point, end_point, color, thickness)
  
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()