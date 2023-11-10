import cv2
import numpy

image_gray = cv2.imread('./images/mandril_gray.tif',cv2.IMREAD_GRAYSCALE)  # reading an image 
print(image_gray.shape)
cv2.imshow('first_image' , image_gray)  # showing an image 
cv2.waitKey()   # waiting 
cv2.destroyAllWindows()  # till pressing anything from keyboard