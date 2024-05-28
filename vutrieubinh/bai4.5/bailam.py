def tinh_ham_phan_phoi_Z(a, b, z):
    if z < 2 * a:
        return 0
    elif z > 2 * b:
        return 1
    else:
        p = 0
        for x in range(a, z - b + 1):
            for y in range(z - x, b + 1):
                p += 1 / ((b - a) ** 2)
        return p

# a,b,c
a = 1
b = 5
z = 7

print("ham phan phoi cua z =", tinh_ham_phan_phoi_Z(a, b, z))
