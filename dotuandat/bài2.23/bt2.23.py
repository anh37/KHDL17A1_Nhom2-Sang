def pdf(x):
    if 2 < x <= 3:
        return 2 * (x - 2)
    return 0

def cdf(x):
    if x <= 2:
        return 0
    elif 2 < x <= 3:
        return (x - 2)**2
    else:
        return 1

# 1. Tìm hàm mật độ xác suất của X
def ham_mat_do(x):
    if 2 < x <= 3:
        return 2 * (x - 2)
    else:
        return 0

# 2. Tính P(1 < X < 1.6)
def xac_suat(a, b):
    return cdf(b) - cdf(a)

# 3. Tính kỳ vọng và phương sai của X
def ky_vong():
    # Tích phân x * pdf(x) từ 2 đến 3
    n = 10000  # số lượng phân đoạn
    a, b = 2, 3  # giới hạn tích phân
    dx = (b - a) / n
    tong = 0
    for i in range(n):
        x = a + i * dx
        tong += x * pdf(x) * dx
    return tong

def phuong_sai():
    ky_vong_val = ky_vong()
    # Tích phân (x^2) * pdf(x) từ 2 đến 3
    n = 10000  # số lượng phân đoạn
    a, b = 2, 3  # giới hạn tích phân
    dx = (b - a) / n
    tong = 0
    for i in range(n):
        x = a + i * dx
        tong += (x ** 2) * pdf(x) * dx
    return tong - ky_vong_val**2

# 4. Tìm Mode của X và các hệ số bất đối xứng, hệ số nhọn của X
def mode():
    return 3  # Vì hàm mật độ xác suất tăng dần trong khoảng (2, 3)

# Tính hệ số bất đối xứng và hệ số nhọn
def he_so_bat_doi_xung():
    ky_vong_val = ky_vong()
    phuong_sai_val = phuong_sai()
    n = 10000  # số lượng phân đoạn
    a, b = 2, 3  # giới hạn tích phân
    dx = (b - a) / n
    tong = 0
    for i in range(n):
        x = a + i * dx
        tong += ((x - ky_vong_val) ** 3) * pdf(x) * dx
    return tong / (phuong_sai_val ** 1.5)

def he_so_nhon():
    ky_vong_val = ky_vong()
    phuong_sai_val = phuong_sai()
    n = 10000  # số lượng phân đoạn
    a, b = 2, 3  # giới hạn tích phân
    dx = (b - a) / n
    tong = 0
    for i in range(n):
        x = a + i * dx
        tong += ((x - ky_vong_val) ** 4) * pdf(x) * dx
    return tong / (phuong_sai_val ** 2) - 3

# Sử dụng ví dụ
print("Hàm mật độ xác suất tại x = 2.5:", ham_mat_do(2.5))
print("Xác suất P(1 < X < 1.6):", xac_suat(1, 1.6))
print("Kỳ vọng của X:", ky_vong())
print("Phương sai của X:", phuong_sai())
print("Mode của X:", mode())
print("Hệ số bất đối xứng của X:", he_so_bat_doi_xung())
print("Hệ số nhọn của X:", he_so_nhon())
