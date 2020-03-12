import cv2
print(cv2.__version__)

image = cv2.imread("download.jpeg", 1)
print(image)
print(image.shape)

print(image[0])
print("~~~~~~~~~~~~~~~")
print(image.shape[0])
print("~~~~~~~~~~~~~~~")
print(len(image))