import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # print(x)
    x = np.asarray(x, dtype=float)
    # print(x)
    return 1/(1+np.exp(-x))