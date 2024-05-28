joint_prob = [
    [0.15, 0.10, 0.14],
    [0.05, 0.20, 0.15],
    [0.01, 0.05, 0.15]
]

Y_values = [100, 200, 300]
X_values = [1, 1.5, 2]

def expectation(values, probabilities):
    return sum(value * prob for value, prob in zip(values, probabilities))

def variance(values, probabilities):
    mean = expectation(values, probabilities)
    return sum((value - mean) ** 2 * prob for value, prob in zip(values, probabilities))

P_Y = [sum(col) for col in zip(*joint_prob)]

E_Y = expectation(Y_values, P_Y)

Var_Y = variance(Y_values, P_Y)

P_X_2 = sum(row[2] for row in joint_prob)
P_Y_300_given_X_2 = joint_prob[2][2] / P_X_2

P_X = [sum(row) for row in joint_prob]

E_X = expectation(X_values, P_X)

def covariance(X_values, Y_values, joint_prob, E_X, E_Y):
    cov = 0
    for i in range(len(X_values)):
        for j in range(len(Y_values)):
            cov += (X_values[i] - E_X) * (Y_values[j] - E_Y) * joint_prob[i][j]
    return cov

Cov_XY = covariance(X_values, Y_values, joint_prob, E_X, E_Y)

Var_X = variance(X_values, P_X)

rho_XY = Cov_XY / (Var_X * Var_Y)**0.5

print("1) Kỳ vọng và phương sai của quảng cáo Y:")
print("Kỳ vọng của Y:", E_Y)
print("Phương sai của Y:", Var_Y)

print("\n2) Xác suất quảng cáo 300 triệu đồng với điều kiện doanh số bán hàng là 2:")
print("P(Y=300 | X=2):", P_Y_300_given_X_2)

print("\n3) Hiệp phương sai và hệ số tương quan giữa X và Y:")
print("Hiệp phương sai Cov(X, Y):", Cov_XY)
print("Hệ số tương quan rho(X, Y):", rho_XY)

print("\n4) Kỳ vọng và phương sai khi doanh số bán hàng là 1.5:")
P_X_1_5 = [row[1] for row in joint_prob]
E_Y_given_X_1_5 = expectation(Y_values, P_X_1_5)
Var_Y_given_X_1_5 = variance(Y_values, P_X_1_5)
print("Kỳ vọng của Y khi X=1.5:", E_Y_given_X_1_5)
print("Phương sai của Y khi X=1.5:", Var_Y_given_X_1_5)
