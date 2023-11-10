import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

values = np.arange(0,256)  # reading value from 0 to 255
values = values.reshape(1 , -1)  # converting 1d values to 2d
repeat = np.repeat(values , repeats=100 , axis = 0) # repeat same row 100 times
# axis 0 means column wise according to NumPy library
plt.imshow(repeat)