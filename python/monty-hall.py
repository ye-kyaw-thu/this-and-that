# -*- coding: utf-8 -*-
"""
Author: Ye Kyaw Thu, Visiting Professor, CADT, Cambodia
Monty Hall problem (i.e. a probability puzzle) simulation
Last Updated: 20 July 2022
"""

import random

def simulate_monty_hall(strategy, num_trials=10000):
    assert strategy in ['switch', 'stick']
    winning_count = 0
    for _ in range(num_trials):
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
            winning_count += 1

    return winning_count / num_trials

print("Probability of winning when switching: ", simulate_monty_hall('switch'))
print("Probability of winning when sticking: ", simulate_monty_hall('stick'))
