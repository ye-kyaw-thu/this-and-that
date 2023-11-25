## Written by Ye Kyaw Thu, LU Lab., Myanmar
## For checking your color knowledge
## Last updated: 26 Nov 2023
## How to run:
## e.g. python color_game.py --num_games 15 --mode hex
## e.g. python color_game.py --help
## e.g. python color_game
## e.g. python ./color_game.py -n 3 -m hex

import tkinter as tk
import random
import matplotlib.colors
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description="Color Guessing Game")
parser.add_argument("-n", "--num_games", type=int, default=10, help="Number of games to play")
parser.add_argument("-m", "--mode", choices=['name', 'hex'], default='name', help="Choose 'name' for color names or 'hex' for hex codes")
args = parser.parse_args()

# Variables for game state
colors = matplotlib.colors.CSS4_COLORS
color_names = list(colors.keys())
total_games = args.num_games
current_game = 0
score = 0
correct_color = ""  # Declare correct_color as a global variable

# Function to generate a random color and options
def get_color_and_options():
    global correct_color
    correct_color = random.choice(color_names)
    options = random.sample(color_names, 2) + [correct_color]
    random.shuffle(options)
    display_options = options if args.mode == 'name' else [colors[name] for name in options]
    return colors[correct_color], display_options

# Function to update the game
def update_game():
    global current_game
    current_game += 1
    if current_game > total_games:
        result_label.config(text=f"Game Over! Your score: {score}/{total_games}")
        for button in option_buttons:
            button.config(state=tk.DISABLED)
        return

    color_hex, options = get_color_and_options()
    canvas.config(bg=color_hex)
    for i in range(3):
        option_buttons[i].config(text=options[i], command=lambda option=options[i]: check_answer(option))
    score_label.config(text=f"Score: {score}/{current_game - 1}")

# Function to check the user's answer
def check_answer(selected_option):
    global score
    correct_answer = correct_color if args.mode == 'name' else colors[correct_color]
    if selected_option == correct_answer:
        score += 1
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text="Wrong!", fg="red")
    update_game()

# Create the main window
root = tk.Tk()
root.title("Color Guessing Game")

# Create a canvas to display the color
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack(pady=20)

# Create buttons for options
option_buttons = [tk.Button(root, text="", width=20) for _ in range(3)]
for button in option_buttons:
    button.pack(pady=5)

# Create labels to show the score and result
score_label = tk.Label(root, text=f"Score: {score}/{current_game}", font=("Helvetica", 14))
score_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

# Initialize the game
update_game()

# Start the GUI loop
root.mainloop()
