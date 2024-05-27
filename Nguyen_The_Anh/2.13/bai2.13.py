# Tìm xác suất của x2
p_x2 = 1 - 0.2
print("Xác suất của x2:", p_x2)

# Tính toán x1 và x2
e_x = 2.6
sigma_x = 0.8
x2 = 4 / 3
a = (e_x - x2 * p_x2) / (0.2 - p_x2)
x1 = a if a > 0 else -a
print("Giá trị của x1:", x1)
print("Giá trị của x2:", x2)

# Phân phối xác suất của X
p_x1 = 0.2
p_x2 = 1 - p_x1
print("Phân phối xác suất của X:")
print(f"P(X = {x1}) = {p_x1}")
print(f"P(X = {x2}) = {p_x2}")
