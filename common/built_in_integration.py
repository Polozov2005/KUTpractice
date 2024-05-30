import numpy as np
from scipy import integrate

import equation

def area():
    h = 0.0001
    x = 0
    x_0 = x

    while equation.radicant(x_0) >= 0:
        x_0 += h
    x_0 += -h
    
    integral = integrate.quad(equation.integrand, 0, x_0)

    result = 4 * integral[0]

    return result

print(area())