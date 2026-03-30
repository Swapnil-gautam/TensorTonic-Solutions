import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    H = 0.0
    d = {}
    n = len(y)
    if n == 0: return 0.0
        
    for i in y:
        # print(p)
        d[i] = d.get(i,0) + 1

    for value in d.values():
        # print(key)
        p = value/n
        if(p != 0):
            H = H - (p * np.log2(p))
    
    return H
    pass