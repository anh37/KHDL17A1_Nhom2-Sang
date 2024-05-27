import numpy as np
from scipy.integrate import quad

# Hàm mật độ xác suất f(x)
def mat_do_xac_suat(x):
    if x <= 0:
        return 0
    elif 0 < x <= 2:
        return x / 4
    else:
        return 4 / x**3

# 1. Tính xác suất chi cho y tế trong năm là trên 3 triệu đồng
def ham_tich_phan_xac_suat_tren_3(x):
    return mat_do_xac_suat(x)

xac_suat_tren_3, _ = quad(ham_tich_phan_xac_suat_tren_3, 3, np.inf)
print(f"Xác suất chi cho y tế trong năm là trên 3 triệu đồng: P(X > 3) = {xac_suat_tren_3}")

# 2. Tính kỳ vọng và phương sai của chi cho y tế hàng năm
def ham_tich_phan_ky_vong(x):
    return x * mat_do_xac_suat(x)

def ham_tich_phan_ky_vong_x2(x):
    return x**2 * mat_do_xac_suat(x)

ky_vong_X, _ = quad(ham_tich_phan_ky_vong, 0, np.inf)
ky_vong_X2, _ = quad(ham_tich_phan_ky_vong_x2, 0, np.inf)
phuong_sai_X = ky_vong_X2 - ky_vong_X**2
print(f"Kỳ vọng E(X) = {ky_vong_X}")
print(f"Phương sai Var(X) = {phuong_sai_X}")
