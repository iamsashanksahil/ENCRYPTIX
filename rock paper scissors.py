print("Task - 3")
import tkinter as tk
from tkinter import messagebox
import random

print("Loading into the game...\n....opening!!")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        
        self.user_score = 0
        self.computer_score = 0
        
        self.create_widgets()
        
    def create_widgets(self):

        self.instructions_label = tk.Label(
            self.root,
            text="Welcome to Rock, Paper, Scissors Game!\n\nChoose Rock, Paper, or Scissors by clicking one of the buttons below.",
            font=("Arial", 12),
            padx=10,
            pady=10
        )
        self.instructions_label.pack()
        
        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play('rock'))
        self.rock_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play('paper'))
        self.paper_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play('scissors'))
        self.scissors_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.score_label = tk.Label(
            self.root,
            text="Score - You: 0, Computer: 0",
            font=("Arial", 12)
        )
        self.score_label.pack(pady=10)
        
        self.feedback_label = tk.Label(
            self.root,
            text="Make your choice and see who wins!",
            font=("Arial", 12),
            fg="blue"
        )
        self.feedback_label.pack(pady=10)

    def play(self, user_choice):
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        if result == "user":
            self.user_score += 1
            feedback_message = f"You chose: {user_choice}\nComputer chose: {computer_choice}\nYou win this round!"
        elif result == "computer":
            self.computer_score += 1
            feedback_message = f"You chose: {user_choice}\nComputer chose: {computer_choice}\nYou lose this round!"
        else:
            feedback_message = f"You chose: {user_choice}\nComputer chose: {computer_choice}\nIt's a tie!"
        
        self.feedback_label.config(text=feedback_message)
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")

        messagebox.showinfo("Round Result", feedback_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()

print("\n\nThanks for playin!")