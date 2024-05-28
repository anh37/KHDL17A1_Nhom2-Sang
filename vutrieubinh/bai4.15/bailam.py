# Hàm mật độ xác suất
def f(x, y):
    # Hàm này trả về giá trị mật độ xác suất của cặp biến (x, y)
    # Trong miền [0, 1]x[0, 1], giá trị mật độ xác suất là tích của x và y
    # Nếu nằm ngoài miền này thì mật độ xác suất là 0
    if 0 <= x <= 1 and 0 <= y <= 1:
        return x * y
    return 0

# Hàm tính mật độ biên của X
def f_X(x):
    # Tích phân hàm mật độ xác suất f(x, y) theo y từ 0 đến 1
    # Điều này cho ta hàm mật độ xác suất của biến X
    integral = 0
    n = 1000  # Số lượng điểm tích phân
    delta_y = 1 / n  # Bước nhảy trong tích phân
    for i in range(n):
        y = i * delta_y
        integral += f(x, y) * delta_y
    return integral

# Hàm tính mật độ biên của Y
def f_Y(y):
    # Tích phân hàm mật độ xác suất f(x, y) theo x từ 0 đến 1
    # Điều này cho ta hàm mật độ xác suất của biến Y
    integral = 0
    n = 1000  # Số lượng điểm tích phân
    delta_x = 1 / n  # Bước nhảy trong tích phân
    for i in range(n):
        x = i * delta_x
        integral += f(x, y) * delta_x
    return integral

# In kết quả hàm mật độ biên của X và Y
print("1) Hàm mật độ biên của X:")
for i in range(10):
    x = i / 10  # Chia khoảng [0, 1] thành 10 điểm
    print(f"f_X({x}) =", f_X(x))

print("\nHàm mật độ biên của Y:")
for i in range(10):
    y = i / 10  # Chia khoảng [0, 1] thành 10 điểm
    print(f"f_Y({y}) =", f_Y(y))