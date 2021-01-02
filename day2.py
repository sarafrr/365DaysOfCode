import numpy as np

def dot_1Dproduct(x, y):
    # assert if the following conditions are not verified
    assert (len(x.shape) == 1 and
            len(x.shape) == len(y.shape))
    out = 0.
    print("shape of x: ", x.shape)
    print(len(x.shape), "-D vector x",sep="")
    print("shape of y: ", y.shape)
    print(len(y.shape), "-D vector y",sep="")
    for i in range(x.shape[0]):
        out += x[i] * y[i]
    print("output: ", out)
    return out

def dot_1D2Dproduct(x, y):
    # assert if the following conditions are not verified
    assert (len(x.shape) == 2 and
            len(y.shape) == 1 and
            x.shape[1]==y.shape[0])
    out = np.zeros(x.shape[0])
    print("shape of x: ", x.shape)
    print(len(x.shape), "-D tensor x",sep="")
    print("shape of y: ", y.shape)
    print(len(y.shape), "-D tensor y",sep="")
    # we fix a row
    # ad we pass the columns (matrix product)
    for i in range(x.shape[0]):
        for j in range(y.shape[0]):
            out[i] += x[i,j] * y[j]
    print("output: ", out)
    return out

# test
x1 = np.array([1,1,1])
y1 = np.array([2,2,2])
x2 = np.ones((4,3))

dot_1Dproduct(x1,y1)
dot_1D2Dproduct(x2,y1)

