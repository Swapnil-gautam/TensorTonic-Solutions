import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    if len(x) != len(y):
        raise ValueError("length of x is not equal to y")
    sum = 0
    # Write code here
    for i,j in zip(x,y):
        sum = sum + (i*j)
    return sum
    pass