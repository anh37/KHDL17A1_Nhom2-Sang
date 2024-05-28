# Giá trị tham số k
k = 6

# Hàm mật độ xác suất đồng thời
def f(x, y, z):
    return k * x * y * z

# Hàm mật độ biên theo x
def f_x(x):
    return k * x

# Hàm mật độ biên theo y
def f_y(y):
    return k * y

# Hàm mật độ biên theo z
def f_z(z):
    return k * z

# Hàm mật độ điều kiện f_xy(x, y)
def f_xy(x, y):
    return f(x, y, 1) / f_z(1)

# Hàm mật độ điều kiện f_xz(x, z)
def f_xz(x, z):
    return f(x, 1, z) / f_y(1)

# In kết quả
print(f"Giá trị tham số k: {k}")
print(f"Hàm mật độ biên theo x: f_x(x) = {f_x(0.5)}")
print(f"Hàm mật độ biên theo y: f_y(y) = {f_y(0.5)}")
print(f"Hàm mật độ biên theo z: f_z(z) = {f_z(0.5)}")
print(f"Hàm mật độ điều kiện f_xy(0.5, 0.5) = {f_xy(0.5, 0.5)}")
print(f"Hàm mật độ điều kiện f_xz(0.5, 0.5) = {f_xz(0.5, 0.5)}")
