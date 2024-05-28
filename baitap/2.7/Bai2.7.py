import numpy as np
import math

# xác suất sản phẩm tốt
san_p_goof = 0.98
p_lot_good = 0.6

# hàm tính xác suất nhị thức
def binom_pmf(k, n, p):
    return math.comb(n, k) * (p * k) * ((1 - p) * (n - k))

# phạm vi số sản phẩm tốt từ máy và từ lô hàng
range_machine = range(3)  
range_lot = range(3)      

# tính phân phối xác suất của X
prob_dist = {}
for x_m in range_machine:
    for x_l in range_lot:
        p_xm = binom_pmf(x_m, 2, san_p_goof)
          # Xác suất P(X_m = x_m)
        p_xl = binom_pmf(x_l, 2, p_lot_good)    
          # Xác suất P(X_l = x_l)
        x = x_m + x_l
        if x in prob_dist:
            prob_dist[x] += p_xm * p_xl
        else:
            prob_dist[x] = p_xm * p_xl

# Cchuyển phân phối xác suất thành danh sách
x_values = list(prob_dist.keys())
probabilities = list(prob_dist.values())

# tính E(X)
E_X = sum(x * p for x, p in prob_dist.items())

# tính V(X)
V_X = sum((x - E_X)**2 * p for x, p in prob_dist.items())

# tính xác suất cho phần 3
p_part3 = prob_dist.get(2, 0)

print("Phân phối xác suất (X, P(X)):", prob_dist)
print("E(X):", E_X)
print("V(X):", V_X)
print("P(X = 2):", p_part3)