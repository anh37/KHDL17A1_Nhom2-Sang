import random
def get_shot_result(p):
    """Mô phỏng kết quả ném rổ của một người."""
    return random.random() <= p
def tinh_phan_phoi_xac_suat(p1, p2):
    """Tính toán bảng phân phối xác suất của X."""
    so_lan_nem = 2  # Số quả ném mỗi người
    so_lan_co_the_xay_ra = range(so_lan_nem + 1)  # Số quả ném trúng rổ của 2 người

    probabilities = []
    for ket_qua in so_lan_co_the_xay_ra:
        so_lan_thanh_cong_cua_nguoi_thu1 = ket_qua  # Số quả ném trúng rổ của người thứ nhất
        so_lan_khong_thanh_cong_cua_nguoi_thu1 = so_lan_nem - so_lan_thanh_cong_cua_nguoi_thu1  # Số quả ném trượt rổ của người thứ nhất

        so_lan_thanh_cong_cua_nguoi_thu2 = ket_qua - so_lan_thanh_cong_cua_nguoi_thu1  # Số quả ném trúng rổ của người thứ hai
        so_lan_khong_thanh_cong_cua_nguoi_thu2 = so_lan_nem - so_lan_thanh_cong_cua_nguoi_thu2  # Số quả ném trượt rổ của người thứ hai

        xac_suat = (p1 ** so_lan_thanh_cong_cua_nguoi_thu1) * ((1 - p1) ** so_lan_khong_thanh_cong_cua_nguoi_thu1) * \
                      (p2 ** so_lan_thanh_cong_cua_nguoi_thu2) * ((1 - p2) ** so_lan_khong_thanh_cong_cua_nguoi_thu2)
        probabilities.append(xac_suat)

    return so_lan_co_the_xay_ra, probabilities
def tinh_kyvong_va_phuongsai(gia_tri_y, xac_suat_y):
    """Tính toán kỳ vọng và phương sai của biến ngẫu nhiên."""
    ky_vong = sum([y * xac_suat for y, xac_suat in zip(gia_tri_y, xac_suat_y)])
    phuong_sai = sum([(y - ky_vong) ** 2 * xac_suat for y, xac_suat in zip(gia_tri_y, xac_suat_y)])
    return ky_vong, phuong_sai
# Xác suất ném trúng rổ của mỗi người
p1 = 0.7  # Người thứ nhất
p2 = 0.8  # Người thứ hai
# Tính toán bảng phân phối xác suất
so_lan_co_the_xay_ra, probabilities = tinh_phan_phoi_xac_suat(p1, p2)
# In bảng phân phối xác suất
print("Bảng phân phối xác suất của X:")
for ket_qua, xac_suat in zip(so_lan_co_the_xay_ra, probabilities):
    print(f"X = {ket_qua}: P(X = {ket_qua}) = {xac_suat:.3f}")
# Xác suất để số quả ném trúng rổ của hai người bằng nhau
xac_suat_bang_nhau = probabilities[1] + probabilities[2]
print(f"\nXác suất để số quả ném trúng rổ của hai người bằng nhau: {xac_suat_bang_nhau:.3f}")
# Tính toán kỳ vọng và phương sai của Y
gia_tri_y = []  # Giá trị của Y
xac_suat_y = []  # Xác suất cho mỗi giá trị của Y
for x in so_lan_co_the_xay_ra:
    y = 2 * x - 5
    gia_tri_y.append(y)

    # Tính toán xác suất cho Y
    if x == 0:
        xac_suat = probabilities[0]
    elif x == 1:
        xac_suat = probabilities[1]
    elif x == 2:
        xac_suat = probabilities[2]
    else:
        xac_suat = 0

    xac_suat_y.append(xac_suat)
# Tính toán kỳ vọng (E(Y))
ky_vong, phuong_sai = tinh_kyvong_va_phuongsai(gia_tri_y, xac_suat_y)
print(f"\nKỳ vọng của Y: E(Y) = {ky_vong:.3f}")
# Tính toán phương sai (Var(Y))
print(f"Phương sai của Y: Var(Y) = {phuong_sai:.3f}")