import cv2
image = cv2.imread('image1.jpg')
#avg
average_blur = cv2.blur(image,(5,5))
#gaus
gaussian_blur = cv2.GaussianBlur(image,(5,5),0)
#median
median_blur=cv2.medianBlur(image,5)
#filter
cv2.imwrite('average_blur.jpg',average_blur)
cv2.imwrite('gaussian_blur.jpg',gaussian_blur)
cv2.imwrite('median_blur.jpg',median_blur)