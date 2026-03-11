import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here

    # pass
    # print(A)  # [[1, 2, 3], [4, 5, 6]]
    A = np.asarray(A)
    # print(A)  # [[1 2 3]
                # [4 5 6]]
    # print(A.shape) (2, 3)
    n,m = A.shape
    At = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            At[i][j] = A[j][i]
    # print(At.shape) (3, 2)

    return At