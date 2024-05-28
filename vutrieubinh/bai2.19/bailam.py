def ham_phan_phoi_F(x):
    if x <= 0:
        return 0
    elif 0 < x <= 1:
        return 2 * x**3 - 3 * x**2 + 2 * x
    else:
        return 1
#xac xuat hanh khach dung lai it nhat la` 20p
def xac_suat_toi_thieu_20_phut():
    thoi_gian = 1 / 3  # 20p = 1/3h
    return 1 - ham_phan_phoi_F(thoi_gian)

#Ham mat do xac xuat cua X
def ham_mat_do_f(x):
    if 0 < x <= 1:
        return 6 * x**2 - 6 * x + 2
    else:
        return 0

#Ky vong X
def tinh_ky_vong_X():
    dx = 0.001  #do rong cua buoc tich phan
    tong = 0
    x = 0
    while x <= 1:
        tong += x * ham_mat_do_f(x) * dx
        x += dx
    return tong

#ky vong cua X^2
def tinh_ky_vong_X2():
    dx = 0.001  #do rong cua buoc tich phan
    tong = 0
    x = 0
    while x <= 1:
        tong += x**2 * ham_mat_do_f(x) * dx
        x += dx
    return tong

#Phuong sai cua X
def tinh_phuong_sai_X():
    E_X = tinh_ky_vong_X()
    E_X2 = tinh_ky_vong_X2()
    return E_X2 - E_X**2

#ket qua
xac_suat_20_phut = xac_suat_toi_thieu_20_phut()
ky_vong_X = tinh_ky_vong_X()
phuong_sai_X = tinh_phuong_sai_X()

print(f"Xac xuat khach hang dung lai it nhat 20p la : {xac_suat_20_phut:.4f}")
print(f"ky vong thoi gian dung lai la : {ky_vong_X:.4f} giờ")
print(f"phuong sai thoi gian dung lai la : {phuong_sai_X:.4f} giờ^2")