import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # the key part was to conver the x to np array once its that then 
    # we dont need to convert or traverse on each element of the list one by one 
    # print(x) # [[-1, 0], [1, 2]]
    x = np.asarray(x, dtype=float)
    # print(x) # [[-1.  0.]
             # [ 1.  2.]]
    return 1/(1+np.exp(-x))