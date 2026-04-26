import random

#random number between 1-20 and the trial counts
mystery_number = random.randint(1,20)
guess_count = 0
guess_limit = 3

#the introductory message
print('''Welcome to the Guessing Game!
      
I'm thinking of a number between 1 and 20. You have 3 attempts
''')

#loop 3 times until you run out or you get the answer
#if you input a number that is higher or lower than the range it will print an error
#if the input is not a number, the program will print an error and retry the code in try
while guess_count < guess_limit:
    try:
        guess = int(input("Enter your guess: "))
        
        if guess < 1 or guess > 20:
            print("Invalid Input")
            continue
    except ValueError:
        print("Input a Numerical Value")
        continue
    
    guess_count += 1
    
    if guess == mystery_number:
        print("You got it! Congratulations!")
        break
    elif guess < mystery_number:
        print("Too Low")
    elif guess > mystery_number:
        print("Too High")
else:
    print(f"Sorry, you ran out of attempts. The correct number was {mystery_number}.")
