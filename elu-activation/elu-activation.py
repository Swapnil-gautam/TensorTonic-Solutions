def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    res = []
    for t in x:
        
        if t > 0:
            res.append(t)
        else:
            res.append(alpha*(math.exp(t) - 1))
    return res
    # Write code here