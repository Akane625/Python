record = {}
    
def save_to_file():
    header = f"{'Lastname':<15}|{'Firstname':^10}|{'Section':^10}|{'Q1':^10}|{'Q2':^10}|{'Q3':^10}|{'Average':>15}\n" + "=" * 90 + "\n"
    header_exists = False
        
    try:
        with open("student record", "r") as fhand:
            line_one = fhand.readline()
            line_two = fhand.readline()
                
            if line_one.strip() == f"{'Lastname':<15}|{'Firstname':^10}|{'Section':^10}|{'Q1':^10}|{'Q2':^10}|{'Q3':^10}|{'Average':>15}" and line_two.strip() == "=" * 90:
                header_exists = True
    except FileNotFoundError:
        pass
        
    with open("student record", "a") as fhand:
        if not header_exists:
            fhand.write(header)
            
        sorting = list(record.keys())
        sorting.sort()
        records = {i: record[i] for i in sorting}
        
        for items, details in records.items():
            fhand.write(f"{items:<15}|{details['firstname']:^10}|{details['section']:^10}|{details['Q1']:^10}|{details['Q2']:^10}|{details['Q3']:^10}|{details['average']:>15}\n")

while True:
    print(f'''{"<Menu>":^15}
[1] Add Record
[2] Search
[3] Modify
[4] Delete
[5] Exit''')
    
    choice = int(input("Choice: "))
    
    if choice == 1:
        lastname = input("\nInput lastname: ").capitalize()
        firstname = input("Input firstname: ").capitalize()
        section = input("Input section: ").upper()
        Q1 = int(input("Input quarter 1 grade: "))
        Q2 = int(input("Input quarter 2 grade: "))
        Q3 = int(input("Input quarter 3 grade: "))
        average = (Q1 + Q2 + Q3) / 3
        
        record[lastname] = {"firstname": firstname, "section": section, "Q1": Q1, "Q2": Q2, "Q3": Q3, "average": average}
        print(f"{lastname} has been added\n")
        
    elif choice == 2:
        lastname = input("\nInput lastname: ").capitalize()
        if lastname in record:
            print(", ".join(str(i) for i in record[lastname].values()))
            print()
        else:
            print("No results found\n")
            continue
        
    elif choice == 3:
        lastname = input("\nInput lastname to modify: ").capitalize()
        if lastname in record:
            Q1 = int(input("Input quarter 1 grade: "))
            Q2 = int(input("Input quarter 2 grade: "))
            Q3 = int(input("Input quarter 3 grade: "))
            average = (Q1 + Q2 + Q3) / 3
            record[lastname] = {"firstname": firstname, "section": section, "Q1": Q1, "Q2": Q2, "Q3": Q3, "average": average}
            print(f"{lastname} updated\n")
        else:
            print("No results found\n")
            continue
            
    elif choice == 4:
        lastname = input("\nInput lastname to remove: ").capitalize()
        if lastname in record:
            del record[lastname]
            print(f"{lastname} has been removed\n")
        else:
            print("No results found\n")
            continue
            
    elif choice == 5:
        print("\nClosing program...")
        save_to_file()
        break
    
    else:
        print("\nInvalid Input\n")
        continue
