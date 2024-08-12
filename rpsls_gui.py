import tkinter as tk
from tkinter import messagebox
import random

# Define choices and rules
choices = ["rock", "paper", "scissors", "lizard", "spock"]
win_conditions = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["rock", "scissors"]
}

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif computer_choice in win_conditions[user_choice]:
        return "You win!"
    else:
        return "You lose!"

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_message = f"Your choice: {user_choice.capitalize()}\nComputer's choice: {computer_choice.capitalize()}\n\n{result}"
    messagebox.showinfo("Result", result_message)

def create_gui():
    root = tk.Tk()
    root.title("Rock, Paper, Scissors, Lizard, Spock")

    # Create buttons for each choice
    for choice in choices:
        button = tk.Button(root, text=choice.capitalize(), command=lambda c=choice: play_game(c))
        button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
