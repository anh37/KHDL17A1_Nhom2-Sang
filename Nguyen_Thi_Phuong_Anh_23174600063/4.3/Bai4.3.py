import numpy as np
import pandas as pd

# numpy : dùng để tính toán                                                                                           

# Bảng phân phối đồng thời của X và Y
phan_phoi_dong_thoi = np.array([[0.15, 0.20, 0.10],[0.35, 0.05, 0.15]])
  # np.array: dùng để tạo mảng từ 1 danh sách hoặc 1 danh sách lồng nhau trong py
  # ([]): mảng 2 chiều -> các phần tử sẽ biểu diễn xác suất đồng thời của các cặp gtri x,y

# Tính phân phối biên của Y
PY = phan_phoi_dong_thoi.sum(axis=1)
print("Phân phối biên của Y:", PY)
  # sum(axis = 1): tính tổng các phần tử theo hàng 

# Tính phân phối biên của X
PX = phan_phoi_dong_thoi.sum(axis=0)
print("Phân phối biên của X:", PX)
   # sum(axis = 0): tính tổng các phần tử theo cột

# Kiểm tra tính độc lập
doc_lap = True
for i in range(phan_phoi_dong_thoi.shape[0]): 
    # .shape[0]: trả về số lượng hàng của mảng 
    for j in range(phan_phoi_dong_thoi.shape[1]):
        #.shape[1]: trả về số lượng cột của mảng 
        if not np.isclose(phan_phoi_dong_thoi[i, j], PX[j] * PY[i]):
            # np.isclose : kiểm tra các giá trị có gần bằng nhau không 
            # phan_phoi_dong_thoi[i, j]: giá trị xuất từ bảng phân phối đồng thời
            # P_X[j] * P_Y[i] : tích của các xác suất -> đúng khi x,y độc lập và ngược lại
            doc_lap = False
            break

print("X và Y có độc lập không?", "Có" if doc_lap else "Không")

# Tính P(X = 1 | Y = 2)
PX_1_cho_Y_2 = phan_phoi_dong_thoi[1, 0] / PY[1]
 # [hàng thứ 2, cột thứ nhất] , (x=1,y=2)

print("P(X = 1 | Y = 2):", PX_1_cho_Y_2)
