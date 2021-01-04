import numpy as np
# reshaping tensors
x = np.array([[1.,2.,3.],
             [4.,5.,6.]])
print(x.shape)
print(x)
x = x.reshape((3,2))
print(x.shape)
print(x)
