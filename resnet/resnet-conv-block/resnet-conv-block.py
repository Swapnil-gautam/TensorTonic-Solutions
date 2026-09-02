import numpy as np

def conv_block(x, W1, W2, Ws):
    # """
    # Returns: np.ndarray with sum of main path output and projected shortcut
    # """
    # # YOUR CODE HERE
    # x = np.array(x)
    # W1 = np.array(W1)
    # W2 = np.array(W2)
    # Ws = np.array(Ws)

    # h = np.maximum(0, x @ (W1))
    # z = np.maximum(0, h @ (W2))
    
    # s = x @ (Ws)

    # y = z+s
    # return y

    # x = np.asarray(x)
    # h = np.maximum(0, x @ np.asarray(W1))   # (2,3) @ (3,4) -> (2,4)
    # z = np.maximum(0, h @ np.asarray(W2))   # (2,4) @ (4,4) -> (2,4)
    # s = x @ np.asarray(Ws)                  # (2,3) @ (3,4) -> (2,4)
    # return z + s

    x = np.asarray(x)
    h = np.maximum(0, x @ np.asarray(W1))   # ReLU inside F
    z = h @ np.asarray(W2)                  # no ReLU here
    s = x @ np.asarray(Ws)
    return np.maximum(0, z + s)   
