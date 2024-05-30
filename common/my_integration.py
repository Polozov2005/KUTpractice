import numpy as np

import equation

def area():
    h = 0.0001
    x = 0
    x_0 = x

    while equation.radicant(x_0) >= 0:
        x_0 += h
    x_0 += -h
    
    integral = integrate(equation.integrand, 0, x_0)

    result = 4 * integral

    return result

def integrate(function, a, b):
    integral = 0
    x = a
    h = np.power(10.0, -5)

    while x < b:
        integral += function(x) * h
        x += h

    return integral