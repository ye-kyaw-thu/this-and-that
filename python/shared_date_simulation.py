"""
Tested by Ye Kyaw Thu, LU Lab., Myanmar.
23 Dec 2024
"""

import random
import argparse

def simulate_probability(num_people, categories, trials=100000):
    matches = 0
    for _ in range(trials):
        outcomes = [random.randint(1, categories) for _ in range(num_people)]
        if len(outcomes) != len(set(outcomes)):
            matches += 1
    return matches / trials

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Simulate probabilities of shared dates.")
    parser.add_argument(
        "num_people",
        type=int,
        help="Number of people for the simulation."
    )
    parser.add_argument(
        "--trials",
        type=int,
        default=100000,
        help="Number of simulation trials to run (default: 100,000)."
    )
    args = parser.parse_args()

    num_people = args.num_people
    trials = args.trials

    # Simulate probabilities
    prob_day_of_week = simulate_probability(num_people, 7, trials)
    prob_month = simulate_probability(num_people, 12, trials)
    prob_birthday = simulate_probability(num_people, 365, trials)

    # Print results
    print(f"Simulated Probability (Same Day of Week, {num_people} people): {prob_day_of_week:.6f}")
    print(f"Simulated Probability (Same Month, {num_people} people): {prob_month:.6f}")
    print(f"Simulated Probability (Same Birthday, {num_people} people): {prob_birthday:.6f}")

if __name__ == "__main__":
    main()

