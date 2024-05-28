import numpy as np
import pandas as pd

phan_phoi_dong_thoi = np.array([[0.15, 0.20, 0.10],[0.35, 0.05, 0.15]])

# Tính phân phối biên của Y
PY = phan_phoi_dong_thoi.sum(axis=1)
print("Phân phối biên của Y:", PY)
 
# Tính phân phối biên của X
PX = phan_phoi_dong_thoi.sum(axis=0)
print("Phân phối biên của X:", PX)

# Kiểm tra tính độc lập
doc_lap = True
for i in range(phan_phoi_dong_thoi.shape[0]): 
    for j in range(phan_phoi_dong_thoi.shape[1]):
        if not np.isclose(phan_phoi_dong_thoi[i, j], PX[j] * PY[i]):
            doc_lap = False
            break

print("X và Y có độc lập không?", "Có" if doc_lap else "Không")

# Tính P(X = 1 | Y = 2)
PX_1_cho_Y_2 = phan_phoi_dong_thoi[1, 0] / PY[1]

print("P(X = 1 | Y = 2):", PX_1_cho_Y_2)
