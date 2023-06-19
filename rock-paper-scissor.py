
import random

print("\nHey there, Let's play rock paper scissor!\n\n")

user_score = 0
bot_score = 0

options = ["rock", "paper", "scissor"]

while True:

    user_choice = input("\nPlease enter one of the following: rock/paper/scissor, or Q to exit the game: ").lower()

    if user_choice == "q":
        break
    
    if user_choice not in options:
        print("Please select a valid option.\n ")
        continue

    computer_choice = random.choice(options)
    # 0 = rock, 1 = paper, 2 = scissor

    print("Computer chose", computer_choice + ".")

    if user_choice == "rock" and computer_choice == "scissor":
        print("You won!")
        user_score += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You won!")
        user_score += 1
    elif user_choice == "scissor" and computer_choice == "paper":
        print("You won!")
        user_score += 1
    else:
        print("Computer won...")
        bot_score += 1
    
    continue

print("\nYour score is:", user_score)
print("Computer score is:", bot_score)

print("\nGoodbye!")

