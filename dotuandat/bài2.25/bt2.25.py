def pdf(x):
    if x <= 0:
        return 0
    elif 0 < x <= 2:
        return x / 4
    else:  # x > 2
        return 4 / (x ** 3)

def cdf(x):
    if x <= 0:
        return 0
    elif 0 < x <= 2:
        return (x ** 2) / 8
    else:  # x > 2
        return 1 - 2 / (x ** 2)

# 1. Tính xác suất chi cho y tế trong năm là trên 3 triệu đồng
def xac_suat_tren_3_trieu():
    return 1 - cdf(3)

# 2. Tính kỳ vọng và phương sai của chi cho y tế hàng năm
def ky_vong():
    # Tích phân x * pdf(x) từ 0 đến vô cực
    n = 10000  # số lượng phân đoạn
    a, b = 0, 100  # giới hạn tích phân, b lớn hơn đủ để đại diện cho vô cực
    dx = (b - a) / n
    tong = 0
    for i in range(n):
        x = a + i * dx
        tong += x * pdf(x) * dx
    return tong

def phuong_sai():
    ky_vong_val = ky_vong()
    # Tích phân (x^2) * pdf(x) từ 0 đến vô cực
    n = 10000  # số lượng phân đoạn
    a, b = 0, 100  # giới hạn tích phân, b lớn hơn đủ để đại diện cho vô cực
    dx = (b - a) / n
    tong = 0
    for i in range(n):
        x = a + i * dx
        tong += (x ** 2) * pdf(x) * dx
    return tong - ky_vong_val**2

# Sử dụng ví dụ
print("Xác suất chi cho y tế trong năm là trên 3 triệu đồng:", xac_suat_tren_3_trieu())
print("Kỳ vọng của chi cho y tế hàng năm:", ky_vong())
print("Phương sai của chi cho y tế hàng năm:", phuong_sai())
