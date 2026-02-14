# Given values
s = 2.67
s1 = 1.00
d = 0.08
T = 20

# Stokes law formula
v = 418 * (s - s1) * (d ** 2) *  (3 * T + 70) /100 

print("Velocity of settlement =", round(v, 3), "mm/sec")
