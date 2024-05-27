# bài 2.17
import numpy as np

# Xác định giá trị của a
a = 1  # Vì integral of a * (1 - 0) = 1 thì a phải bằng 1

# Tính xác suất P(1/4 < X < 1/2)
P = a * (1/2 - 1/4)
print(f"Xác suất P(1/4 < X < 1/2): {P}")

# Xác định hàm phân phối xác suất F(x)
def F(x):
    if x < 0:
        return 0
    elif 0 <= x <= 1:
        return x
    else:
        return 1

# Kiểm tra hàm F(x) với các giá trị khác nhau
x_values = [-0.5, 0.25, 0.5, 1.5]
F_values = [F(x) for x in x_values]

print("Hàm phân phối xác suất F(x) với các giá trị x tương ứng:")
for x, Fx in zip(x_values, F_values):
    print(f"F({x}) = {Fx}")
