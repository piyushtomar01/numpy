import numpy as np
 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
 
newarr = arr.reshape(arr.shape[0], -1)
print(newarr)