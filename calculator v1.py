choice = int(input("Input month (1-12): "))

if choice == 1:
    print(f"{'January 2024':^{50}}\nSun\t\tMon\t\tTues\tWed\t\tThur\tFri\t\tSat\n" + "\t\t" * 1, end = "")
    for i in range(1,32):
        print(i, end = "\t\t" if (i + 1) % 7 else "\n")
elif choice == 2:
    print(f"{'February 2024':^{50}}\nSun\t\tMon\t\tTues\tWed\t\tThur\tFri\t\tSat\n" + "\t\t" * 4, end = "")
    for i in range(1,30):
        print(i, end = "\t\t" if (i + 4) % 7 else "\n")
elif choice == 3:
    print(f"{'March 2024':^{50}}\nSun\t\tMon\t\tTues\tWed\t\tThur\tFri\t\tSat\n" + "\t\t" * 5, end = "")
    for i in range(1,32):
        print(i, end = "\t\t" if (i + 5) % 7 else "\n")
elif choice == 4:
    print(f"{'April 2024':^{50}}\nSun\t\tMon\t\tTues\tWed\t\tThur\tFri\t\tSat\n" + "\t\t" * 1, end = "")
    for i in range(1,31):
        print(i, end = "\t\t" if (i + 1) % 7 else "\n")
elif choice == 5:
    print(f"{'May 2024':^{50}}\nSun\t\tMon\t\tTues\tWed\t\tThur\tFri\t\tSat\n" + "\t\t" * 1, end = "")
    for i in range(1,32):
        print(i, end = "\t\t" if (i + 1) % 7 else "\n")
elif choice == 6:
    print(f"{'June 2024':^{50}}\nSun\t\tMon\t\tTues\tWed\t\tThur\tFri\t\tSat\n" + "\t\t" * 6, end = "")
    for i in range(1,31):
        print(i, end = "\t\t" if (i + 6) % 7 else "\n")
elif choice == 7:
    print(f"{'July 2024':^{50}}\nSun\t\tMon\t\tTues\tWed\t\tThur\tFri\t\tSat\n" + "\t\t" * 1, end = "")
    for i in range(1,32):
        print(i, end = "\t\t" if (i + 1) % 7 else "\n")
elif choice == 8:
    print(f"{'August 2024':^{50}}\nSun\t\tMon\t\tTues\tWed\t\tThur\tFri\t\tSat\n" + "\t\t" * 4, end = "")
    for i in range(1,32):
        print(i, end = "\t\t" if (i + 4) % 7 else "\n")
elif choice == 9:
    print(f"{'September 2024':^{50}}\nSun\t\tMon\t\tTues\tWed\t\tThur\tFri\t\tSat")
    for i in range(1,31):
        print(i, end = "\t\t" if i % 7 else "\n")
elif choice == 10:
    print(f"{'October 2024':^{50}}\nSun\t\tMon\t\tTues\tWed\t\tThur\tFri\t\tSat\n" + "\t\t" * 2, end = "")
    for i in range(1,32):
        print(i, end = "\t\t" if (i + 2) % 7 else "\n")
elif choice == 11:
    print(f"{'November 2024':^{50}}\nSun\t\tMon\t\tTues\tWed\t\tThur\tFri\t\tSat\n" + "\t\t" * 4, end = "")
    for i in range(1,31):
        print(i, end = "\t\t" if (i + 4) % 7 else "\n")
elif choice == 12:
    print(f"{'December 2024':^{50}}\nSun\t\tMon\t\tTues\tWed\t\tThur\tFri\t\tSat")
    for i in range(1,32):
        print(i, end = "\t\t" if i % 7 else "\n")
else:
    print("Invalid Input")
