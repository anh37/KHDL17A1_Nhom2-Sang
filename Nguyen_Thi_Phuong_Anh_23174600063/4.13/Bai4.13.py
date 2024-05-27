#1.Kiểm tra tính chất của hàm mật độ xác suất đồng thời
import sympy as sp

x,y = sp.symbols('x y')
f = sp.exp(-x-y)
integral = sp.integrate (f ,(x, 0, sp.oo), (y, 0, sp.oo))
print(integral)

#2. Xác định hàm phân phối xác suất đồng thời
F = sp.integrate (f , (x, 0, x),(y, 0, y))
print(F)

#3.Xác định các mật độ biên và phân phối biên của các thành phần
f_X = sp.integrate ( f, (y, 0, sp.oo))
f_Y = sp.integrate ( f, (x, 0, sp.oo))
print(f_X)
print(f_Y)

# 4.xác định hàm mật độ có điều kiện
f_Y_cho_X = f / f_X
f_X_cho_Y = f / f_Y
print(f_X_cho_Y)

# 5. P(X<= Y <= c) với c = ln2
c = sp.ln(2)
P1 = sp.integrate(sp.integrate(f, (x, 0, y)),(y, 0, c))
print(P1)

# 6.P(X,Y) và P(X+Y<=3)
P_X_nhỏ_Y = sp.integrate(sp.integrate(f, ( x,0,y)), (y,0,sp.oo))
P_X_cộng_Y_nho_bang_3 = sp.integrate(sp.integrate(f, (x,0,3-y)),(y,0,3))

print(P_X_nhỏ_Y)
print(P_X_cộng_Y_nho_bang_3)




