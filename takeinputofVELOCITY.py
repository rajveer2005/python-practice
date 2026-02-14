s = float(input("Enter specific gravity of particle: "))
s1 = float(input("Enter specific gravity of water: "))
d = float(input("Enter diameter (mm): "))
T = float(input("Enter temperature (°C): "))

v = 418 * (s - s1) * (d ** 2) *  (3 * T + 70) / 100

print("Velocity of settlement =", round(v, 3), "mm/sec")
