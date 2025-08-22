import cv2
image = cv2.imread('image1.jpg')
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite('grayscale_image.jpg',gray_image)