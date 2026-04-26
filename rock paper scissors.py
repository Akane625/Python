import random
import time

choices = "rock paper scissors"
player_points = 0
bot_points = 0


print("Rock, Paper, Scissors\n")


while True:
    try:
        player_choice = input("").lower()
        if player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
            pass
        else:
            print("Invalid Input\n")
            continue
    except ValueError:
        print("Invalid Input\n")
    
    choice = choices.split()
    bot_choice = random.choice(choice)
    print(bot_choice)
    
    if player_choice.lower() == bot_choice:
        print("Tie\n")
    elif player_choice.lower() == "rock" and bot_choice == "paper":
        print("Bot gets a point\n")
        bot_points += 1
    elif player_choice.lower() == "rock" and bot_choice == "scissors":
        print("Player gets a point\n")
        player_points += 1
    elif player_choice.lower() == "paper" and bot_choice == "rock":
        print("Player gets a point\n")
        player_points += 1
    elif player_choice.lower() == "paper" and bot_choice == "scissors":
        print("Bot gets a point\n")
        bot_points += 1
    elif player_choice.lower() == "scissors" and bot_choice == "rock":
        print("Bot gets a point\n")
        bot_points += 1
    elif player_choice.lower() == "scissors" and bot_choice == "paper":
        print("Player gets a point\n")
        player_points += 1
        
    print(f"You: {player_points} | Bot: {bot_points}\n")
        
    if player_points == 3:
        system_message_one = "WOW YOU WON THATS CRAZY GO GET A LIFE BRO"
        message_one = system_message_one.split()
        for i in message_one:
            print(i, end = " ", flush = True)
            time.sleep(0.1)
        break
    elif bot_points == 3:
        system_message_two = "HAHAHA YOU LOST TO A BASIC BOT WTF YOU SUCK"
        message_two = system_message_two.split()
        for i in message_two:
            print(i, end = " ", flush = True)
            time.sleep(0.1)
        break
        break
