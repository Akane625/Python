calculations_history = []
unique_materials = set()
units = ('N', 'm²', 'm', 'm', ' Pascals (Pa)', ' (dimensionless)')
counter = 1

while True:
    try:
        material = input("What material is used: ")
        force = float(input("What is the force (N): "))
        area = float(input("What is the cross-sectional area (m²): "))
        original = float(input("What is the original length (m): "))
        change = float(input("What is the change in length (m): "))
    except ValueError:
        print("Invalid input. Restarting input phase...")
        continue

    history = {f'Transaction {counter}': [material, force, area, original, change]}
    counter += 1
    calculations_history.append(history)
    unique_materials.add(material)

    choice = input("\nAdd more items (Yes/No): ")
    if choice.lower() == 'yes':
        continue
    elif choice.lower() == 'no':
        break
    else:
        print("Invalid input. Ending input phase...")
        break

for i in calculations_history:
    for j in i.values():
        try:
            stress = j[1] / j[2]
            strain = j[4] / j[3]

            j.append(stress)
            j.append(strain)
        except ZeroDivisionError:
            print("Cannot divide by zero. Moving to next transaction...")

for i in calculations_history:
    for j in i.values():
        print(f'''\nMaterial: {j[0]}
        Force: {j[1]}{units[0]}
        Cross-Sectional Area: {j[2]}{units[1]}
        Original Length: {j[3]}{units[2]}
        Change in Length: {j[4]}{units[3]}
        Stress: {j[5]}{units[4]}
        Strain: {j[6]}{units[5]}
        \n''')

print(f"Unique Materials Used: {", ".join(map(str, unique_materials))}")
