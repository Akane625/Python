import random
import sys
import time
import re

points_1 = 0
points_2 = 0
goal = 30
        
def naming_rule():
    while True:
        player_1 = input(">Input first player's name: ")
        if not re.match("^[A-Za-z ]+$", player_1):
            print("PLayer 1's name cannot contain numbers and symbols\n")
            continue
        
        player_2 = input(">Input second player's name: ")
        if not re.match("^[A-Za-z ]+$", player_2):
            print("PLayer 2's name cannot contain numbers and symbols\n")
            continue
        
        if player_1.lower() == player_2.lower():
            print("NAMES ARE NOT ALLOWED TO BE THE SAME\n")
        else:
            return player_1, player_2

player_1, player_2 = naming_rule()

while True:
    roll_1 = input("\n\n\n>Input 'r' to roll: ")
    if roll_1.lower() == "r":
        for i in range(10):
            dice_1 = random.randint(1, 6)
            sys.stdout.write(f"\r{dice_1}")
            sys.stdout.flush()
            time.sleep(0.1)
        points_1 += dice_1
        if dice_1 == 1:
            points_1 = 0
    else:
        print("Invalid Input")
        
    print(f"\n>{player_1} points: {points_1}")
    
    roll_2 = input("\n\n\n>Input 'r' to roll: ")
    if roll_2.lower() == "r":
        for i in range(10):
            dice_2 = random.randint(1, 6)
            sys.stdout.write(f"\r{dice_2}")
            sys.stdout.flush()
            time.sleep(0.1)
        points_2 += dice_2
        if dice_2 == 1:
            points_2 = 0
    else:
        print("Invalid Input")
        
    print(f"\n>{player_2} points: {points_2}")
    
    if points_1 >= goal:
        print(f"{player_1} wins!!!")
        break
    elif points_2 >= goal:
        print(f"{player_2} wins!!!")
        break
