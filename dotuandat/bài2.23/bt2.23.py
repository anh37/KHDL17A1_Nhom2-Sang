import numpy as np
from scipy.integrate import quad

# Hàm mật độ xác suất f(x)
def mat_do_xac_suat(x):
    if 2 < x <= 3:
        return 2 * (x - 2)
    else:
        return 0

# 1. Tìm hàm mật độ xác suất của X (đã có)
print("Hàm mật độ xác suất f(x) đã được định nghĩa.")

# 2. Tính P(1 < X < 1,6)
def ham_tich_phan_P(x):
    return mat_do_xac_suat(x)

xac_suat_1_1_6, _ = quad(ham_tich_phan_P, 1, 1.6)
print(f"P(1 < X < 1,6) = {xac_suat_1_1_6}")

# 3. Tính kỳ vọng và phương sai của X
def ham_tich_phan_ky_vong(x):
    return x * mat_do_xac_suat(x)

def ham_tich_phan_ky_vong_x2(x):
    return x**2 * mat_do_xac_suat(x)

ky_vong_X, _ = quad(ham_tich_phan_ky_vong, 2, 3)
ky_vong_X2, _ = quad(ham_tich_phan_ky_vong_x2, 2, 3)
phuong_sai_X = ky_vong_X2 - ky_vong_X**2
print(f"Kỳ vọng E(X) = {ky_vong_X}")
print(f"Phương sai Var(X) = {phuong_sai_X}")

# 4. Tìm Mode của X và các hệ số bất đối xứng, hệ số nhọn của X
# Mode của X là điểm mà hàm mật độ xác suất đạt giá trị lớn nhất, trong khoảng (2, 3) hàm f(x) tăng dần nên Mode là 3.
mode_X = 3
print(f"Mode của X = {mode_X}")

# Hệ số bất đối xứng (Skewness)
def ham_tich_phan_bat_doi_xung(x):
    return ((x - ky_vong_X)**3) * mat_do_xac_suat(x)

he_so_bat_doi_xung, _ = quad(ham_tich_phan_bat_doi_xung, 2, 3)
he_so_bat_doi_xung /= phuong_sai_X**(3/2)
print(f"Hệ số bất đối xứng (Skewness) = {he_so_bat_doi_xung}")

# Hệ số nhọn (Kurtosis)
def ham_tich_phan_he_so_nhon(x):
    return ((x - ky_vong_X)**4) * mat_do_xac_suat(x)

he_so_nhon, _ = quad(ham_tich_phan_he_so_nhon, 2, 3)
he_so_nhon /= phuong_sai_X**2
he_so_nhon -= 3
print(f"Hệ số nhọn (Kurtosis) = {he_so_nhon}")
