import numpy as np
# element wise operations
def elem_wise_1DAddition(x,y):
    # assert if the following conditions are not verified
    assert (len(x.shape)==1 and len(x.shape) == len(y.shape))
    out = np.zeros(x.shape[0])
    print("shape of x: ", x.shape)
    print("length of x: ", len(x.shape))
    print("shape of y: ", y.shape)
    print("length of y: ", len(y.shape))
    for i in range(0,x.shape[0]):
        out[i] = x[i]+y[i]
    print("output vector: ", out)
    return out

# broadcasting operations
def broadcasting_addition(x,y):
    # assert if the following conditions are not verified
    print("shape of x: ", x.shape)
    print("length of x: ", len(x.shape))
    print("shape of y: ", y.shape)
    print("length of y: ", len(y.shape))
    out = x+y
    print("output vector: ", out)
    return out

# test
x1 = np.array([1,1,1])
y1 = np.array([2,2,2])
z1 = np.array([2])
elem_wise_1DAddition(x1,y1)
# the one one element of z is broadcasted to have the same
# dimension of the other summed array (vector-1D tensor)
broadcasting_addition(x1,z1)
x2 = np.array([[1,1,1],
              [1,1,1]])
# the one one element of z is broadcasted to have the same
# dimension of the other summed array (matrix-2D tensor)
broadcasting_addition(x2,z1)
