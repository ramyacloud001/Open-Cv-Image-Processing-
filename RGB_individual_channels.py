import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 


color_img = plt.imread('./images/h.jpg')
plt.subplot(2,2,1)
plt.title('R_channel')
plt.imshow(color_img[: , : , 0] , cmap='gray')
plt.subplot(2,2,2)
plt.title('G_channel')
plt.imshow(color_img[: , : , 1] , cmap='gray')
plt.subplot(2,2,3)
plt.title('B_channel')
plt.imshow(color_img[: , : , 2] , cmap='gray')
plt.subplot(2,2,4)
plt.title('Original_color_image')
plt.imshow(color_img)