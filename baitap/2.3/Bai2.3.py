# 1.Xác suất để thí sinh đó đỗ cả ba vòng
p1 = 0.8
p2 = 0.6
p3 = 0.55

allpass = p1 * p2 * p3
print(f"Xác suất để thí sinh đó đỗ qua cả 3 vòng là: {allpass :.3f}") 

# 2.Lập bảng phân phối xác suất các vòng
#Xác suất đỗ 0 vòng
P0 = (1 - p1) * (1 - p2) * (1 - p3)
#Xác suất đỗ 1 vòng
P1 = (p1 * (1 - p2) * (1 - p3)) + ((1 - p1) * p2 * (1 - p3)) + ((1 - p1) * (1 - p2) * p3)
#Xác suất đỗ 2 vòng
P2 = (p1 * p2 * (1 - p3)) + (p1 * (1 - p2) * p3) + ((1 - p1) * p2 * p3)
#Xác suất đỗ cả 3 vòng
P3 = p1 * p2 * p3

distribution = {
    0: P0,
    1: P1,
    2: P2,
    3: P3
} #Tạo bảng phân phối xác suất

print("Bảng phân phối xác suất cho số vòng thi đỗ của thí sinh:")
for x, p in distribution.items(): 
    print(f"Số vòng đỗ = {x}: Xác suất = {p:.3f}")

# 3.
# kì vọng
E_x = sum( x*p for x,p in distribution.items())
print(f"Kì vọng của số vòng thi đỗ: {E_x: .2f}")

E_x2 = sum( x**2 * p for x, p in distribution.items())
# phương sai
V_x = E_x2 - E_x**2
print(f"Phương sai của số vòng thi đỗ : {V_x: .3f}")