import random

# User input
user_choice = input("Your choice (rock, paper, or scissors): ").lower()


choices = ["rock", "paper", "scissors"]

if user_choice in choices:
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
        print("You won!")
    elif user_choice == computer_choice:
        print("It's a tie!")
    else:
        print("You lost.")
else:
    print("Invalid choice. Please type 'rock', 'paper', or 'scissors'.")
