import numpy as np

# Số lần thử mở cửa
n_trials = 4

# Xác suất thành công (mở được cửa)
p_success = 1 / n_trials

# Tính phân phối xác suất của X (số lần thử mở cửa)
X_values = np.arange(1, n_trials + 1)
X_probabilities = np.array([p_success * (1 - p_success) ** (x - 1) for x in X_values])

# In phân phối xác suất của X
print("Phân phối xác suất của X:")
for i in range(len(X_values)):
    print("X =", X_values[i], ":", X_probabilities[i])

# Tính kì vọng của X
mean_X = np.sum(X_values * X_probabilities)
print("\nKì vọng của X:", mean_X)

# Tính phương sai của X
var_X = np.sum((X_values - mean_X) ** 2 * X_probabilities)
print("Phương sai của X:", var_X)

# Tìm mốt của X
mode_X = X_values[np.argmax(X_probabilities)]
print("\nMốt của X:", mode_X)
