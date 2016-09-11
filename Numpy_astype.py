import numpy as np

x = np.array([[1,2,3], [4,5,6]], np.int32)
print(x.shape)
x.shape = (6,)
print(x)
x = x.astype('int64')
print(x.dtype)
