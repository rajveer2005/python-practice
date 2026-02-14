# Taking input from user
pH = float(input("Enter pH value: "))
caustic_alkalinity = float(input("Enter caustic alkalinity (mg/L): "))
total_alkalinity = float(input("Enter total alkalinity (mg/L): "))
total_hardness = float(input("Enter total hardness (mg/L): "))

# Step 1: Carbonate alkalinity
carbonate_alkalinity = 2 * caustic_alkalinity

# Step 2: Bicarbonate alkalinity
bicarbonate_alkalinity = total_alkalinity - carbonate_alkalinity

# Step 3: Non-carbonate hardness
non_carbonate_hardness = total_hardness - total_alkalinity

# Output
print("\nResults:")
print("Carbonate alkalinity =", carbonate_alkalinity, "mg/L")
print("Bicarbonate alkalinity =", bicarbonate_alkalinity, "mg/L")
print("Non-carbonate hardness =", non_carbonate_hardness, "mg/L")
