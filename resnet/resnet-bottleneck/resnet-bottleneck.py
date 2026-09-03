import numpy as np

# def bottleneck_block(x, W1, W2, W3, Ws):
#     """
#     Returns: np.ndarray with bottleneck residual block output (compress, process, expand + skip)
#     """
#     # YOUR CODE HERE
#     x = np.array(x) # 4, 2
#     W1 = np.array(W1) # 2, 4
#     W2 = np.array(W2) # 2, 2
#     W3 = np.array(W3) # 6, 2
#     Ws = np.array(Ws) # 6, 4
#     # output 6, 2
    
#     return np.maximum(0, W3@(np.maximum(0, W2@(np.maximum(0, W1@x)))).T) + Ws @ x
#     pass

#     import numpy as np

def bottleneck_block(x, W1, W2, W3, Ws):
    x = np.array(x, dtype=float)
    W1 = np.array(W1, dtype=float)
    W2 = np.array(W2, dtype=float)
    W3 = np.array(W3, dtype=float)
    if Ws is not None:
        Ws = np.array(Ws, dtype=float)
        identity = x @ Ws
    else:
        identity = x.copy()
    out = np.maximum(0, x @ W1)
    out = np.maximum(0, out @ W2)
    out = out @ W3
    result = np.maximum(0, out + identity)
    return [[round(float(v), 4) for v in row] for row in result]
