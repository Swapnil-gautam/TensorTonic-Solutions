import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.asarray(x, dtype = float)
    p = np.asarray(p, dtype = float)
    if(np.sum(p) < 1-(10 ** -6)):
        raise ValueError("probabilities don't sum to 1")
    if(x.shape == p.shape):
        return np.sum(x*p)
    else:
        raise ValueError("n and p dimensions mismatch")
    pass
