import random

words = ["math", "english", "science"]
random_word = random.choice(words)
guesses = []
turns = 0

while turns < 5:
    #list comprehension [output iterate condition]
    display = ''.join([letter if letter in guesses else '_' for letter in random_word])
    print(display)
    
    guess = input("Guess a letter: ").lower()
    
    if guess in words:
        guesses.append(guess)
        if set(guesses) >= set(random_word):
            print(f"You guessed the word {random_word}!")
            break
    else:
        turns += 1
        print(f"Wrong guess. {turns} turns left.")
    
if turns == 5:
    print(f"\nYou lost! The word was {random_word}.")
