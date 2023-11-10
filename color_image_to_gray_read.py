import cv2
import numpy

image_gray = cv2.imread('./images/mandril_color.tif',cv2.IMREAD_GRAYSCALE)  # reading an image 
print(image_gray.shape)
cv2.imshow('first_image' , image_gray)  # showing an image 
cv2.waitKey()   # waiting 
cv2.destroyAllWindows()  # till pressing anything from keyboard

# cv2.IMREAD_GRAYSCALE  -  you can use 0 also instead of cv2.IMREAD_GRAYSCALE