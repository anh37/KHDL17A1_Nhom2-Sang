a = 1  
b = 2  

def f_X(x, a, b):
    if a < x < b:
        return 1 / (b - a)
    else:
        return 0

def f_Y(y, a, b):
    if y > 0:
        x = math.log(y)
        if a < x < b:
            return 1 / ((b - a) * y)
    return 0

def f_Z(z, a, b):
    x = math.exp(z)
    if a < x < b:
        return math.exp(z) / (b - a)
    return 0

import math

y_value = 3  
z_value = 0.5  

pdf_Y = f_Y(y_value, a, b)
print(f"PDF of Y = e^X at Y = {y_value}: {pdf_Y}")

pdf_Z = f_Z(z_value, a, b)
print(f"PDF of Z = ln(X) at Z = {z_value}: {pdf_Z}")
