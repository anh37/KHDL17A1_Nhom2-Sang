import numpy as np

# Xác định các xác suất đã cho
prob_matrix = np.array([
    [0.10, 0.05, 0.05],
    [0.10, 0.20, 0.05],
    [0.05, 0.10, 0.35]
])
p = 0.10  # Đã tính ở trên

# Xác suất biên của X
px = np.sum(prob_matrix, axis=1)
# Xác suất biên của Y
py = np.sum(prob_matrix, axis=0)

# Kỳ vọng của X và Y
x_values = np.array([10, 15, 20])
y_values = np.array([0, 5, 10])

E_X = np.sum(x_values * px)
E_Y = np.sum(y_values * py)

# Kỳ vọng của XY
xy_matrix = np.outer(x_values, y_values) * prob_matrix
E_XY = np.sum(xy_matrix)

# Hiệp phương sai
cov_XY = E_XY - E_X * E_Y

# Phương sai của X và Y
E_X2 = np.sum((x_values**2) * px)
var_X = E_X2 - E_X**2

E_Y2 = np.sum((y_values**2) * py)
var_Y = E_Y2 - E_Y**2

# Hệ số tương quan
corr_XY = cov_XY / np.sqrt(var_X * var_Y)

# Kỳ vọng và phương sai của lương khi Y = 5
cond_prob_X_given_Y5 = prob_matrix[:, 1] / py[1]
E_X_given_Y5 = np.sum(x_values * cond_prob_X_given_Y5)
E_X2_given_Y5 = np.sum((x_values**2) * cond_prob_X_given_Y5)
var_X_given_Y5 = E_X2_given_Y5 - E_X_given_Y5**2

# Kỳ vọng, phương sai và độ lệch chuẩn của Z
E_Z = E_X + E_Y
var_Z = var_X + var_Y + 2 * cov_XY
std_Z = np.sqrt(var_Z)

print(f"Xác suất p: {p}")
print(f"Phân phối biên của X: {px}")
print(f"Phân phối biên của Y: {py}")
print(f"Kỳ vọng của X: {E_X}")
print(f"Kỳ vọng của Y: {E_Y}")
print(f"Hiệp phương sai: {cov_XY}")
print(f"Hệ số tương quan: {corr_XY}")
print(f"Kỳ vọng của X khi Y = 5: {E_X_given_Y5}")
print(f"Phương sai của X khi Y = 5: {var_X_given_Y5}")
print(f"Kỳ vọng của Z: {E_Z}")
print(f"Phương sai của Z: {var_Z}")
print(f"Độ lệch chuẩn của Z: {std_Z}")
