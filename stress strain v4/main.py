from stress_strain.core.calculator import compute_stress, compute_strain, compute_youngs_modulus, stats, plot
from stress_strain.io.file_ops import export_csv
import pandas as pd

record = {'Materials': [], 'Force': [], 'Area': [], 'Length': [], 'Change': [], 'Stress (Pa)': [],
          'Strain': [], "Young's Modulus (Pa)": [], 'Stress (psi)': [], "Young's Modulus (psi)": []}

while True:
    try:
        material = input("Enter material: ")
        force = float(input("Enter force (N) of material: "))
        area = float(input("Enter cross-sectional area (m²) of material: "))
        length = float(input("Enter original length (m) of material: "))
        change = float(input("Enter change in length (m) of material: "))
    except ValueError:
        print("Please enter a valid number")
        continue

    if area <= 0 or length <= 0:
        print("Cross-sectional area or original length cannot be negative or zero")
        continue

    stress = compute_stress(force, area)
    strain = compute_strain(change, length)
    young_modulus = compute_youngs_modulus(stress, strain)
    stress_psi = stress / 6894.757
    young_psi = young_modulus / 6894.757

    for i, j in zip(record.keys(), [material, force, area, length, change, stress, strain, young_modulus, stress_psi, young_psi]):
        record[i].append(j)

    print(f'''
    REPORT
    Inputs = Force: {force}N, Cross-Sectional Area: {area}m², Original Length: {length}m, Change in Length: {change}m
    Calculations (Pascals) = Stress: {stress:.4f} Pa, Strain: {strain:.4f} (dimensionless), Young's Modulus: {young_modulus:.4f} Pa
    Unit Conversions (Pounds per Square Inch) = Stress: {stress_psi:.4f} psi, Young's Modulus: {young_psi:.4f} psi
    ''')

    choice = input("\nWould you like to enter a new set of data (yes/no): ")  #
    if choice.lower() == "yes":
        continue
    elif choice.lower() == "no":
        break
    else:
        print("Invalid choice. Ending program")
        break

export_csv(record)
df = pd.read_csv("Stress_Strain_Record.csv")
print("\nCurrent Session:")
print(stats({'Stress (Pa)': record['Stress (Pa)'], 'Strain': record['Strain']}))
print("\nRecord (CSV):")
print(stats({'Stress (Pa)': df['Stress (Pa)'], 'Strain': df['Strain']}))
print(plot(df['Stress (Pa)'], df['Strain']))
