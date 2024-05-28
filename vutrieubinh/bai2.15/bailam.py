import math 

# Tham số tỉ lệ hỏng của bóng đèn
ti_le_hong = 0.01

# Tính xác suất bóng đèn hoạt động tốt trước t0 giờ
def xac_suat_truoc_t0(t0, ti_le_hong):
    return 1 - math.exp(-ti_le_hong * t0)

# Tính kỳ vọng của thời gian hoạt động tốt
def ky_vong_thoi_gian_hoat_dong(ti_le_hong):
    return 1 / ti_le_hong

# Ví dụ sử dụng
t0 = 100  # giá trị t0 có thể thay đổi tùy theo yêu cầu
xac_suat = xac_suat_truoc_t0(t0, ti_le_hong)
ky_vong = ky_vong_thoi_gian_hoat_dong(ti_le_hong)

print(f"Xác suất bóng đèn hoạt động tốt trước {t0} giờ: {xac_suat:.4f}")
print(f"Kỳ vọng của thời gian hoạt động tốt: {ky_vong:.2f} giờ")