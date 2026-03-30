import numpy as np

def cal_mt(m, beta1, grad):
    return (beta1*m + (1-beta1)*grad)

def cal_vt(v, beta2, grad):
    return (beta2*v + (1-beta2)*grad*grad)

def bias_mt(m, t, beta1):
    return m / (1 - (beta1 ** t))

def bias_vt(v, t, beta2):
    return v / (1 - (beta2 ** t))

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    grad = np.asarray(grad, dtype=float)
    param = np.asarray(param, dtype=float)
    m = np.asarray(m, dtype=float) 
    v = np.asarray(v, dtype=float) 

    m = cal_mt(m, beta1, grad)
    m_hat = bias_mt(m, t, beta1)
    v = cal_vt(v, beta2, grad)
    v_hat = bias_vt(v, t, beta2)

    param = param - lr * (m_hat / (np.sqrt(v_hat) + eps))
    
    return (param, m, v)
    
    
    pass