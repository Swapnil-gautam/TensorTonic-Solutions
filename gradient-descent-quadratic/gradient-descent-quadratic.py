# Write code here
def funcx(a, b, c, x0):
    return (a*x0*x0 + b*x0 + c)

def derfuncx(a, b, c, x0):
    return (2*a*x0 + b)

def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    for i in range(steps):
        der = derfuncx(a, b, c, x0)
        x0 = x0 - (lr * der)
        # print("x0:", x0, " der:", der)

    return x0
    pass