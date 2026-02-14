# Given values
pH = 9
caustic_alkalinity = 70
total_alkalinity = 230
total_hardness = 300

# Carbonate alkalinity
carbonate_alkalinity = 2 * caustic_alkalinity

# Bicarbonate alkalinity
bicarbonate_alkalinity = total_alkalinity - carbonate_alkalinity

# Non-carbonate hardness
non_carbonate_hardness = total_hardness - total_alkalinity

# Output
print("Carbonate alkalinity =", carbonate_alkalinity, "mg/L")
print("Bicarbonate alkalinity =", bicarbonate_alkalinity, "mg/L")
print("Non-carbonate hardness =", non_carbonate_hardness, "mg/L")
