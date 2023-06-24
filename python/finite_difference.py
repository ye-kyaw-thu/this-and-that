# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 19:35:33 2023

@author: Ye Kyaw Thu, LST, NECTEC, Thailand.
Finite Difference

How to run:
    python finite_difference.py 3
    python finite_difference.py 4
    python finite_difference.py 5

References:
https://warwick.ac.uk/fac/sci/dcs/research/em/publications/web-em/02/babbage.pdf
https://en.wikipedia.org/wiki/Difference_engine    
"""

import argparse

def calculate_square(n):
    # Initialize the table of f(x) and differences
    x_values = list(range(1, n+2))
    fx_values = [x**2 for x in x_values]
    #print("x_values: ", x_values)
    #print("fx_values:", fx_values)
    first_differences = [fx_values[i+1]-fx_values[i] for i in range(len(fx_values)-1)]
    second_differences = [first_differences[i+1]-first_differences[i] for i in range(len(first_differences)-1)]
    
    # Print the table
    print("x\tf(x)\t1st diff\t2nd diff")
    for i in range(n):
        print(f"{x_values[i]}\t{fx_values[i]}\t", end="")
        if i < len(first_differences):
            print(f"{first_differences[i]}\t", end="")
        if i < len(second_differences):
            print(f"{second_differences[i]}", end="")
        print()
    
    # Calculate the next value of f(x) using the method of finite differences
    next_first_difference = first_differences[-1] + second_differences[-1]
    next_fx_value = fx_values[-1] + next_first_difference
    print("\nCalculation:")
    print("next_first_difference = first_differences[-1] + second_differences[-1]")
    print(f"{next_first_difference} = {first_differences[-1]} + {second_differences[-1]}")
    print("next_fx_value = fx_values[-1] + next_first_difference")
    print(f"{next_fx_value} = {fx_values[-1]} + {next_first_difference}")
    print(f"\nThe square of {n+1} is {next_fx_value} according to the method of finite differences.")

# Parse command-line argument
parser = argparse.ArgumentParser(description='Calculate the square of a number using the method of finite differences.')
parser.add_argument('n', type=int, help='The number to calculate the square of.')
args = parser.parse_args()

# Call the function with the command-line argument
calculate_square(args.n)
