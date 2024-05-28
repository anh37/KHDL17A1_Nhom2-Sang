# Bảng phân phối xác suất đồng thời
# Y = [2, 2.5, 4]
# X = [1.5, 2, 3]
# P(X, Y)
probabilities = [
    [3, 2, 0],  # X=1.5
    [2, 2, 0],  # X=2
    [1, 2, 0]   # X=3
]

# Tính phân phối xác suất biên của X
def phan_phoi_X(probabilities):
    phan_phoi_X_values = []
    for row in probabilities:
        phan_phoi_X_values.append(sum(row))
    return phan_phoi_X_values

# Tính phân phối xác suất biên của Y
def phan_phoi_Y(probabilities):
    phan_phoi_Y_values = [0] * len(probabilities[0])
    for row in probabilities:
        for j, value in enumerate(row):
            phan_phoi_Y_values[j] += value
    return phan_phoi_Y_values

# Tính P(X|Y) và P(Y|X)
def xac_suat_dieu_kien(probabilities):
    P_X_given_Y = []
    P_Y_given_X = []
    phan_phoi_X_values = phan_phoi_X(probabilities)
    phan_phoi_Y_values = phan_phoi_Y(probabilities)
    
    for i, row in enumerate(probabilities):
        P_X_given_Y_row = []
        P_Y_given_X_row = []
        for j, value in enumerate(row):
            P_X_given_Y_row.append(value / phan_phoi_Y_values[j])
            P_Y_given_X_row.append(value / phan_phoi_X_values[i])
        P_X_given_Y.append(P_X_given_Y_row)
        P_Y_given_X.append(P_Y_given_X_row)
    
    return P_X_given_Y, P_Y_given_X

# In kết quả
P_X_given_Y, P_Y_given_X = xac_suat_dieu_kien(probabilities)
print("Phân phối xác suất biên của X:")
print(f"P(X=1.5) = {P_X_given_Y[0][0]:.2f}")
print(f"P(X=2) = {P_X_given_Y[1][0]:.2f}")
print(f"P(X=3) = {P_X_given_Y[2][0]:.2f}\n")

print("P(X|Y):")
for i, row in enumerate(P_X_given_Y):
    print(f"P(X={i+1.5}|Y=2) = {row[0]:.2f}")
    print(f"P(X={i+1.5}|Y=2.5) = {row[1]:.2f}")
    print(f"P(X={i+1.5}|Y=4) = {row[2]:.2f}\n")

print("P(Y|X):")
for i, row in enumerate(P_Y_given_X):
    print(f"P(Y=2|X={i+1.5}) = {row[0]:.2f}")
    print(f"P(Y=2.5|X={i+1.5}) = {row[1]:.2f}")
    print(f"P(Y=4|X={i+1.5}) = {row[2]:.2f}\n")
