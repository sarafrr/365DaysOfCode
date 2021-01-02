import numpy as np
# element wise operations
def elem_wise_1DAddition(x,y):
    # assert if the following conditions are not verified
    assert (len(x.shape)==1 and len(x.shape) == len(y.shape))
    out = np.zeros(x.shape[0])
    print("shape of x: ", x.shape)
    print(len(x.shape),"-D vector x")
    print("shape of y: ", y.shape)
    print(len(y.shape),"-D vector y")
    # range begins by default from 0 if we set one only index
    for i in range(x.shape[0]):
        out[i] = x[i]+y[i]
    print("output vector: ", out)
    return out

# broadcasting operations
def broadcasting_addition(x,y):
    # there is not necessity to assert for the different dimension
    # of the arrays for the broadcasting of the operations
    print("shape of x: ", x.shape)
    print(len(x.shape),"-D vector x")
    print("shape of y: ", y.shape)
    print(len(y.shape),"-D vector y")
    out = x+y
    print("output vector: ", out)
    return out

# test
x1 = np.array([1,1,1])
y1 = np.array([2,2,2])
# the one element array can be specified without square brackets
z1 = np.array(2)
elem_wise_1DAddition(x1,y1)
# the one element of z is broadcasted to have the same
# dimension of the other summed array (vector-1D tensor)
broadcasting_addition(x1,z1)
x2 = np.array([[1,1,1],
              [1,1,1]])
# the one element of z is broadcasted to have the same
# dimension of the other summed array (matrix-2D tensor)
broadcasting_addition(x2,z1)
