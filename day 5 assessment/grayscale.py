import cv2
image=cv2.imread('image1.jpg')
#convert gray scale
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite('grays scale_image.jpg',gray_image)