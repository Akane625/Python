while True:
    try:
        force = float(input("Enter Applied Force (in Newtons): "))
        area = float(input("Enter Cross-Sectional Area (in Square Meters): "))
        length = float(input("Enter Original Length of the Material (in Meters): "))
        change = float(input("Enter Change in Length (in Meters): "))
    except ValueError:
        print("Invalid input. Restarting")
        continue

    try:
        stress = force / area
        strain = change / length
    except ZeroDivisionError:
        print("Cannot divide by zero. Restarting program")
        continue

    print(f"\nStress (Pa): {stress} Pascals (Pa)")
    print(f"Strain: {strain} (dimensionless)\n")\

    convert = input("Convert Stress to psi (Yes/No): ")
    if convert.lower() == "yes":
        print(f"Stress (psi): {stress / 6895} Pounds per Square Inch (psi)")
        print(f"Young's Modulus: {stress} / {strain} Pascals (PA)\n")
    elif convert.lower() == "no":
        pass
    else:
        print("Input not in range. Moving on")

    again = str(input("Try a new set of values (Yes/No): "))
    if again.lower() == "yes":
        continue
    elif again.lower() == "no":
        break
    else:
        print("Input not in range. Ending program")
