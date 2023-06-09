# -*- coding: utf-8 -*-
"""
Author: Ye Kyaw Thu, Visiting Professor, CADT, Cambodia
Monty Hall simulation, for this time the program will run 10 games and after that, show the probabilities between "sticking" and "switching".  
Last Updated: 26 July 2022
"""

import random

def simulate_single_monty_hall(strategy):
    assert strategy in ['switch', 'stick']
    doors = [0, 0, 1]  # 0 is a goat, 1 is a car
    random.shuffle(doors)  # Randomly place the car

    # Contestant's initial choice
    choice = random.choice([0, 1, 2])

    # Monty opens a door
    monty_opens = [i for i in range(3) if doors[i] == 0 and i != choice][0]

    # Switch doors if strategy is 'switch'
    if strategy == 'switch':
        choice = [i for i in range(3) if i != choice and i != monty_opens][0]

    # Check if the contestant won
    if doors[choice] == 1:
        return True  # Contestant won the car
    else:
        return False  # Contestant got a goat


# Initialize counter variables
switch_wins = 0
stick_wins = 0
games_count = 10

for game_number in range(1, games_count+1):  # For 10 games
    print("\nGame number: ", game_number)

    # Track wins when switching
    if simulate_single_monty_hall('switch'):
        print("Result when switching: Won the car!")
        switch_wins += 1
    else:
        print("Result when switching: Got a goat!")

    # Track wins when sticking
    if simulate_single_monty_hall('stick'):
        print("Result when sticking: Won the car!")
        stick_wins += 1
    else:
        print("Result when sticking: Got a goat!")

# Print winning probabilities
print("\nProbability of winning when switching: ", switch_wins/games_count)
print("Probability of winning when sticking: ", stick_wins/games_count)
