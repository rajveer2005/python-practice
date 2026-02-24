import math
import matplotlib.pyplot as plt


def display_line():
    print("-" * 60)


def display_question_table(population, sewage_per_capita, detention_time, depth):
    print("\n----- QUESTION TABLE -----")
    print(f"{'Parameter':<30}{'Value'}")
    display_line()
    print(f"{'Population':<30}{population}")
    print(f"{'Sewage per capita (LPCD)':<30}{sewage_per_capita}")
    print(f"{'Detention Time (hr)':<30}{detention_time}")
    print(f"{'Effective Depth (m)':<30}{depth}")
    display_line()


def primary_clarifier_design(population, sewage_per_capita, detention_time, depth):
    print("\n----- STEPWISE SOLUTION -----")

    # 1) Daily Flow
    daily_flow_litres = population * sewage_per_capita
    daily_flow_m3 = daily_flow_litres / 1000

    print(f"\n1) Daily Flow = Population × Sewage per capita")
    print(f"   = {population} × {sewage_per_capita}")
    print(f"   = {daily_flow_litres} litres")
    print(f"   = {daily_flow_m3:.3f} m³")

    # 2) Tank Capacity
    tank_capacity = (daily_flow_m3 / 24) * detention_time
    print(f"\n2) Tank Capacity = (Daily Flow / 24) × Detention Time")
    print(f"   = ({daily_flow_m3:.3f} / 24) × {detention_time}")
    print(f"   = {tank_capacity:.3f} m³")

    # 3) Surface Area
    surface_area = tank_capacity / depth
    print(f"\n3) Surface Area = Tank Capacity / Depth")
    print(f"   = {tank_capacity:.3f} / {depth}")
    print(f"   = {surface_area:.3f} m²")

    # 4) Dimensions (L/B = 4)
    b = math.sqrt(surface_area / 4)
    l = 4 * b

    print(f"\n4) Assume L/B = 4")
    print(f"   L × B = {surface_area:.3f}")
    print(f"   B = {b:.3f} m")
    print(f"   L = {l:.3f} m")

    # 5) Overflow Rate
    overflow_rate = daily_flow_m3 / surface_area
    print(f"\n5) Overflow Rate = Daily Flow / Surface Area")
    print(f"   = {daily_flow_m3:.3f} / {surface_area:.3f}")
    print(f"   = {overflow_rate:.3f} m³/m²-day")

    # Answer Table
    print("\n----- ANSWER TABLE -----")
    display_line()
    print(f"{'Parameter':<30}{'Value'}")
    display_line()
    print(f"{'Daily Flow (m³)':<30}{round(daily_flow_m3,3)}")
    print(f"{'Tank Capacity (m³)':<30}{round(tank_capacity,3)}")
    print(f"{'Surface Area (m²)':<30}{round(surface_area,3)}")
    print(f"{'Length (m)':<30}{round(l,3)}")
    print(f"{'Breadth (m)':<30}{round(b,3)}")
    print(f"{'Overflow Rate (m³/m²-day)':<30}{round(overflow_rate,3)}")
    display_line()

    # Graph (Overflow Rate Check)
    plt.figure()
    plt.axhline(40)
    plt.axhline(50)
    plt.scatter(1, overflow_rate)
    plt.title("Surface Overflow Rate Check")
    plt.ylabel("Overflow Rate (m³/m²-day)")
    plt.xticks([])
    plt.show()


# ---------------- MAIN PROGRAM ---------------- #

while True:
    print("\n====== PRIMARY CLARIFIER DESIGN ======")
    print("1. Run with SAME values as in picture")
    print("2. Enter your own values")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        population = 34000
        sewage_per_capita = 150
        detention_time = 2
        depth = 2.5

        display_question_table(population, sewage_per_capita, detention_time, depth)
        primary_clarifier_design(population, sewage_per_capita, detention_time, depth)

    elif choice == "2":
        population = float(input("Enter Population: "))
        sewage_per_capita = float(input("Enter Sewage per capita (LPCD): "))
        detention_time = float(input("Enter Detention Time (hr): "))
        depth = float(input("Enter Effective Depth (m): "))

        display_question_table(population, sewage_per_capita, detention_time, depth)
        primary_clarifier_design(population, sewage_per_capita, detention_time, depth)

    elif choice == "3":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice! Try again.")