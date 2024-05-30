import numpy as np

def radicant(x):
    a = 0.8
    c = 0.7

    if x == 0:
        result = 0.0

    else:
        result = np.sqrt(np.power(a, 4) + 4 * np.square(c) * np.square(x)) - np.square(x) - np.square(a)

    return result

def integrand(x):
    result = np.sqrt(radicant(x))

    return result