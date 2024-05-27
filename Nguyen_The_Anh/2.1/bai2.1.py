import random

# Tạo ra các giá trị ngẫu nhiên cho 10 vận động viên
thoi_gian = [random.gauss(50, 5) for _ in range(10)]  # 50 phút là giá trị trung bình, 5 phút là độ lệch chuẩn
thu_tu_ve_dich = list(range(1, 11))  # [1, 2, 3, ..., 10]
random.shuffle(thu_tu_ve_dich)  # Trộn danh sách ngẫu nhiên
toc_do = [random.gauss(35, 5) for _ in range(10)]  # 35 km/h là giá trị trung bình, 5 km/h là độ lệch chuẩn
tien_thuong = [random.choice([5000, 3000, 2000, 1000, 500]) for _ in range(10)]

# In kết quả
print("Thời gian hoàn thành (phút):", thoi_gian)
print("Thứ tự về đích:", thu_tu_ve_dich)
print("Tốc độ (km/h):", toc_do)
print("Số tiền thưởng (USD):", tien_thuong)