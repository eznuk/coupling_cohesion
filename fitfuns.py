import numpy as np

def exp_fit(t, a):
    """
    Exponential function
    """
    return t ** a

def sin_fit(t, a, b):
    """
    Sinusoidal function
    """
    return np.sin(t) * a + b