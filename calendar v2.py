months_data = [
    ("January", 31, 1), ("February", 29, 4), ("March", 31, 5), ("April", 30, 1),
    ("May", 31, 1), ("June", 30, 6), ("July", 31, 1), ("August", 31, 4),
    ("September", 30, 0), ("October", 31, 2), ("November", 30, 4), ("December", 31, 0)
]

choice = int(input("Input month (1-12): "))

if 1 <= choice <= 12:
    month_name, num_days, start_day_offset = months_data[choice - 1]

    print(f"{month_name} 2024".center(50))
    print("Sun\t\tMon\t\tTues\tWed\t\tThur\tFri\t\tSat")
    
    print("\t\t" * start_day_offset, end="")

    for i in range(1, num_days + 1):
        print(i, end="\t\t" if (i + start_day_offset) % 7 else "\n")
else:
    print("Invalid Input")
