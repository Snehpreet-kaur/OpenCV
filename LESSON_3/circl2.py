## Using thickness of -1 px to fill the circle by red color. 

import cv2
image = cv2.imread("pika.png")
window_name = 'Image'
center_coordinates = (120, 100)
radius = 30
color = (0, 0, 255)
thickness = -1
image = cv2.circle(image, center_coordinates, radius, color, thickness)
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
