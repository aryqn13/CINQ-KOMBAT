import random

def get_user_choice():
    print("Enter your choice (rock, paper, scissors, lizard, spock):")
    user_choice = input().lower()
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    while user_choice not in choices:
        print("Invalid choice. Please choose one of: rock, paper, scissors, lizard, spock")
        user_choice = input().lower()
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    win_conditions = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["paper", "spock"],
        "spock": ["rock", "scissors"]
    }

    if user_choice == computer_choice:
        return "It's a tie!"
    elif computer_choice in win_conditions[user_choice]:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
