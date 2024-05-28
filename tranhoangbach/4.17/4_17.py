import math

mu_X = 2.2
sigma_X = 0.4
mu_Y = 2.5
sigma_Y = 0.6
rho_XY = -0.5

E_X = mu_X
E_Y = mu_Y
Var_X = sigma_X ** 2
Var_Y = sigma_Y ** 2

Cov_XY = rho_XY * sigma_X * sigma_Y

# a) Xác suất tổng số thời gian học và thời gian chơi lớn hơn 5 giờ
E_Z = E_X + E_Y
Var_Z = Var_X + Var_Y + 2 * Cov_XY

z_score = (5 - E_Z) / math.sqrt(Var_Z)

P_Z_gt_5 = 1 - 0.5 * (1 + math.erf(z_score / math.sqrt(2)))

# b) Xác suất thời gian học lớn hơn thời gian chơi
E_W = E_X - E_Y
Var_W = Var_X + Var_Y - 2 * Cov_XY

z_score_W = (0 - E_W) / math.sqrt(Var_W)

P_W_gt_0 = 1 - 0.5 * (1 + math.erf(z_score_W / math.sqrt(2)))

print("a) Xác suất tổng số thời gian học và thời gian chơi lớn hơn 5 giờ:", P_Z_gt_5)
print("b) Xác suất thời gian học lớn hơn thời gian chơi:", P_W_gt_0)
