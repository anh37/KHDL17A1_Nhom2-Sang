import math
# Định nghĩa hàm phân phối xác suất đồng thời
def F_xy(x, y):
    if 0 <= x <= math.pi/2 and 0 <= y <= math.pi/2:
        return math.sin(x) + math.sin(y)
    else:
        return 0
# Tính hàm mật độ xác suất biên của X
def f_X(x):
    if 0 <= x <= math.pi/2:
        return math.cos(x)
    else:
        return 0
# Tính hàm mật độ xác suất biên của Y
def f_Y(y):
    if 0 <= y <= math.pi/2:
        return math.cos(y)
    else:
        return 0
# Hiển thị kết quả
print("Hàm mật độ xác suất biên của X:", f_X)
print("Hàm mật độ xác suất biên của Y:", f_Y)
# Tính xác suất được yêu cầu
P = 0
delta = 0.01  # Bước xấp xỉ
for x in range(int(math.pi/4/delta), int(math.pi/3/delta)):
    for y in range(int(math.pi/6/delta), int(math.pi/2/delta)):
        x_val = x * delta
        y_val = y * delta
        P += F_xy(x_val, y_val) * delta * delta

# Hiển thị kết quả
print("Xác suất P:", P)