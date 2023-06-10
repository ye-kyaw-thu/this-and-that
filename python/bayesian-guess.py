# -*- coding: utf-8 -*-
"""
Author: Ye Kyaw Thu, Visiting Professor, CADT, Cambodia
Bayesian Belief or Bayesian Guess
Last Updated: 28 July 2022
"""

import random
import matplotlib.pyplot as plt
import numpy as np

def update_prior(guess, prior, too_high):
    scale = 3 # This is a hyperparameter you could tune
    if too_high:
        likelihood = np.array([np.exp(-0.5 * ((g - guess) / scale) ** 2) for g in range(1, 101)])
        likelihood[guess <= np.arange(1, 101)] = 0
    else:
        likelihood = np.array([np.exp(-0.5 * ((guess - g) / scale) ** 2) for g in range(1, 101)])
        likelihood[guess >= np.arange(1, 101)] = 0
    prior *= likelihood
    prior /= np.sum(prior)  # normalize
    return prior

def plot_prior(prior):
    plt.plot(range(1, 101), prior)
    plt.title('Current belief about player\'s guess')
    plt.xlabel('Number')
    plt.ylabel('Probability')
    plt.show()

def bayesian_guessing_game():
    # Computer picks a number
    number = random.randint(1, 100)

    # Set up prior
    prior = np.ones(100) / 100

    print("Welcome to the Bayesian Guessing Game!")
    print("The computer has picked a number between 1 and 100.")
    print("After each guess, you'll see a graph showing the current belief about your guess.")
    print("The X-axis is the number and the Y-axis shows how likely the computer thinks that number is the correct one based on your previous guesses.")
    print("Let's start the game!\n")

    while True:
        # Show current belief
        plot_prior(prior)

        # print the current most probable number
        most_probable_number = np.argmax(prior) + 1
        print(f"The computer believes the most probable number is: {most_probable_number}")

        # Player makes a guess
        guess = int(input('Guess a number from 1 to 100: '))
        if guess < 1 or guess > 100:
            print('Out of range. Please try again.')
            continue

        # Check the guess
        if guess < number:
            print('Too low.')
            prior = update_prior(guess, prior, too_high=False)
        elif guess > number:
            print('Too high.')
            prior = update_prior(guess, prior, too_high=True)
        else:
            print('Correct!')
            break

# Play the game
bayesian_guessing_game()
