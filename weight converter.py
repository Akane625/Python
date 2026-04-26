weight = int(input('Weight(in kg): '))
unit = input('(P)ounds or (G)rams: ')
if unit.upper() == "P":
    pounds = 2.205 * weight
    print(f'You are {pounds} pounds')
else:
    grams = 1000 * weight
    print(f'You are {grams} grams')
