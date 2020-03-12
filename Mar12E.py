import cv2
import numpy as np

image = cv2.imread("download.jpeg", 0)
rotatedimage = np.rot90(image)
cv2.imshow("any", image)
cv2.waitKey(2000)
cv2.imshow("rott", rotatedimage)
cv2.waitKey(5000)