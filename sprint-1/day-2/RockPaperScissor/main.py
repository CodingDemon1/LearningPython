import random

game_options = ["rock", "paper", "scissors"]

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice
      

def get_computer_choice():
    return random.choice(game_options)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

user_score = 0
computer_score = 0
draws = 0

while True:

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer choice: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)

    if winner == "user":
        user_score += 1
        print("You win this round!")
    elif winner == "computer":
        computer_score += 1
        print("Computer wins this round!")
    else:  
        draws += 1
        print("It's a draw!")

    print(f"Scores: User-{user_score}, Computer-{computer_score}, Draws-{draws}")

    play_again = input("Do you want to play another round? (yes/no) ").lower()
    if play_again != "yes":
        print("See you Again!")
        break  
