import numpy as np
import math

# Hàm mật độ xác suất đồng thời
def f(x, y):
    if x > 0 and y > 0:
        return math.exp(-x - y)
    else:
        return 0

# Kiểm tra tính chất của hàm mật độ xác suất đồng thời
def check_density():
    x = np.linspace(0, 10, 1000)
    y = np.linspace(0, 10, 1000)
    dx = x[1] - x[0]
    dy = y[1] - y[0]
    integral = sum(f(xi, yi) * dx * dy for xi in x for yi in y)
    return integral

# Hàm phân phối xác suất đồng thời
def F(x, y):
    if x > 0 and y > 0:
        return 1 - math.exp(-x) - math.exp(-y) + math.exp(-x - y)
    else:
        return 0

# Mật độ biên của X
def f_X(x):
    if x > 0:
        return math.exp(-x)
    else:
        return 0

# Mật độ biên của Y
def f_Y(y):
    if y > 0:
        return math.exp(-y)
    else:
        return 0

# Hàm mật độ có điều kiện của X cho Y = y
def f_X_given_Y(x, y):
    if x > 0 and y > 0:
        return f(x, y) / f_Y(y)
    else:
        return 0

# Hàm mật độ có điều kiện của Y cho X = x
def f_Y_given_X(y, x):
    if x > 0 and y > 0:
        return f(x, y) / f_X(x)
    else:
        return 0

# Tính P(X ≤ Y ≤ c) với c = ln2
def P_X_le_Y_le_c(c):
    x = np.linspace(0, c, 1000)
    y = np.linspace(0, c, 1000)
    dx = x[1] - x[0]
    dy = y[1] - y[0]
    sum_value = 0
    for xi in x:
        for yi in y:
            if xi <= yi:
                sum_value += f(xi, yi) * dx * dy
    return sum_value

# Tính P(X < Y)
def P_X_lt_Y():
    x = np.linspace(0, 10, 1000)
    y = np.linspace(0, 10, 1000)
    dx = x[1] - x[0]
    dy = y[1] - y[0]
    sum_value = 0
    for xi in x:
        for yi in y:
            if xi < yi:
                sum_value += f(xi, yi) * dx * dy
    return sum_value

# Tính P(X + Y ≤ 3)
def P_X_plus_Y_le_3():
    x = np.linspace(0, 3, 1000)
    dx = x[1] - x[0]
    sum_value = 0
    for xi in x:
        y = np.linspace(0, 3 - xi, 1000)
        dy = y[1] - y[0]
        for yi in y:
            sum_value += f(xi, yi) * dx * dy
    return sum_value

# Main function
if __name__ == "__main__":
    print(f"Integral value (should be 1): {check_density()}")
    print(f"F(1, 1): {F(1, 1)}")
    print(f"f_X(1): {f_X(1)}")
    print(f"f_Y(1): {f_Y(1)}")
    print(f"f_X_given_Y(1, 1): {f_X_given_Y(1, 1)}")
    print(f"f_Y_given_X(1, 1): {f_Y_given_X(1, 1)}")
    
    c = math.log(2)
    print(f"P(X <= Y <= c): {P_X_le_Y_le_c(c)}")
    print(f"P(X < Y): {P_X_lt_Y()}")
    print(f"P(X + Y <= 3): {P_X_plus_Y_le_3()}")