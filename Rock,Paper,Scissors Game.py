import random
import tkinter as tk

def get_Partner_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(Your_choice, Partner_choice):
    if Your_choice == Partner_choice:
        return "It's a tie!"
    elif (
        (Your_choice == "rock" and Partner_choice == "scissors") or
        (Your_choice == "paper" and Partner_choice == "rock") or
        (Your_choice == "scissors" and Partner_choice == "paper")
    ):
        return "You win!"
    else:
        return "Partner wins!"

def play_game():
    Your_choice = Your_choice_var.get().lower()
    Partner_choice = get_Partner_choice()
    result = determine_winner(Your_choice, Partner_choice)
    result_label.config(text=f"You chose {Your_choice}.\nPartner chose {Partner_choice}.\n{result}")

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

Your_choice_label = tk.Label(root, text="Enter your choice (Rock/Paper/Scissors):")
Your_choice_label.pack()

Your_choice_var = tk.StringVar()
Your_choice_entry = tk.Entry(root, textvariable=Your_choice_var)
Your_choice_entry.pack()

play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

result_label = tk.Label(root, text="", wraplength=500)
result_label.pack()

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack()

root.mainloop()
