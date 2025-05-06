## Using thickness of -1 px to fill the rectangle by black color.
import cv2
image = cv2.imread("pika.png", 0)
start_point = (100, 50)
end_point = (125, 80)
color = (0, 0, 0)
thickness = -1
image = cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
