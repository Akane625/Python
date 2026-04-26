record = {}

def display():
    print(f"\n{'Products':<15}|{'Quantity':^10}|{'Price':^10}|{'Total Amount':>15}")
    print("=" * 55)
    
    sorting = list(record.keys())
    sorting.sort()
    records = {i: record[i] for i in sorting}
    
    for items, details in records.items():
        print(f"{items:<15}|{details['quantity']:^10}|{details['price']:^10}|{details['total']:>15}")
    print()
    
def save_to_file():
    with open("inventory", "a") as fhand:
        fhand.write(f"{'Products':<15}|{'Quantity':^10}|{'Price':^10}|{'Total Amount':>15}\n")
        fhand.write("=" * 55 + "\n")
        
        sorting = list(record.keys())
        sorting.sort()
        records = {i: record[i] for i in sorting}
        
        for items, details in records.items():
            fhand.write(f"{items:<15}|{details['quantity']:^10}|{details['price']:^10}|{details['total']:>15}\n")

while True:
    print('''<Inventory Management System>
    [1] Add Product
    [2] Remove Product
    [3] Update Product
    [4] Display Inventory
    [5] Exit''')
    
    choice = int(input("Choice: "))
    
    if choice == 1:
        product = input("\nInput product: ").capitalize()
        quantity = int(input("Input quantity: "))
        price = float(input("Input price: "))
        total = quantity * price
        
        record[product] = {"quantity": quantity, "price": price, "total": total}
        print(f"{product} has been added\n")
        
    elif choice == 2:
        product = input("\nInput product to remove: ").capitalize()
        if product in record:
            del record[product]
            print(f"{product} has been removed\n")
        else:
            print("No results found\n")
            continue
        
    elif choice == 3:
        product = input("\nInput product to update: ").capitalize()
        if product in record:
            quantity = int(input("Input new quantity: "))
            total = quantity * price
            record[product] = {"quantity": quantity, "price": price, "total": total}
            print(f"{product} updated\n")
        else:
            print("No results found\n")
            continue
            
    elif choice == 4:
        if len(record) > 0: 
            display()
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
