database = {'steel': {"young's modulus": 200, 'yield strength': 307.5},
            'titanium': {"young's modulus": 105, 'yield strength': 327.5},
            'aluminum': {"young's modulus": 70, 'yield strength': 338}}  # young in Gpa and yield in Mpa


def validate_input(data):
    try:
        if float(data) < 0:
            return False
        return data
    except ValueError:
        return False


def calculate_stress(forces, areas):
    try:
        stress = forces / areas
        return stress
    except ZeroDivisionError:
        print('Zero division error detected. Outputs are invalid')
        return None


def calculate_strain(changes, originals):
    try:
        strain = changes / originals
        return strain
    except ZeroDivisionError:
        print('Zero division error detected. Outputs are invalid')
        return None


def calculate_young_modulus(stresses, strains):
    try:
        if stresses is None or strains is None:
            raise ZeroDivisionError
        young_modulus = stresses / strains
        return young_modulus
    except ZeroDivisionError:
        print('Zero division error detected. Outputs are invalid')
        return None


def main_calculator():
    while True:
        material = input("What material is used: ")
        force = input("What is the force (N): ")
        area = input("What is the cross-sectional area (m²): ")
        original = input("What is the original length (m): ")
        change = input("What is the change in length (m): ")

        if material.lower() not in database.keys():
            print(f"\n{material.capitalize()} does not match database\n")
            continue

        for i in [force, area, original, change]:
            if not validate_input(i):
                print(f"\nOnly non-negative integers are allowed. Restarting input phase\n")
                return main_calculator()
        break
    return material.lower(), float(force), float(area), float(original), float(change)


a, b, c, d, e = main_calculator()
stress_value = calculate_stress(b, c)
strain_value = calculate_strain(e, d)
modulo_value = calculate_young_modulus(stress_value, strain_value)

if stress_value is None or strain_value is None or modulo_value is None:
    print("Shutting down program...")
else:
    print(f'''
    Material: {a}
    Force: {b}N
    Cross-Sectional Area: {c}m²
    Original Length: {d}m
    Change in Length: {e}m
    Stress: {stress_value} Pascals (Pa)
    Strain: {strain_value} (dimensionless)
    Young's Modulus: {modulo_value} Pascals (Pa)
    
    CALCULATED '{a.upper()}' vs. DATABASE '{a.upper()}'
    Young Modulus: {modulo_value / (10**9)} Gpa vs. {database[a]["young's modulus"]} Gpa
    Likely to Fail: {'Yes' if (stress_value / (10**6)) > database[a]['yield strength'] else 'No'}, {stress_value / (10**6)} Mpa vs. {database[a]['yield strength']} Mpa
    ''')
