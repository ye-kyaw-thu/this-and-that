"""
Tested by Ye Kyaw Thu, LU Lab., Myanmar.
23 Dec 2024
"""

import argparse
from math import factorial

def probability_same_weekday(num_people, days_in_week=7):

    if num_people > days_in_week:
        return 1.0  # If more people than days in a week, there must be a match.

    # Calculate the probability that no one shares a weekday.
    prob_no_shared = 1.0
    for i in range(num_people):
        prob_no_shared *= (days_in_week - i) / days_in_week

    # Probability of at least one shared weekday
    return 1 - prob_no_shared

def probability_same_month(num_people, months_in_year=12):

    if num_people > months_in_year:
        return 1.0  # If more people than months, there must be a match.

    # Calculate the probability that no one shares a birth month.
    prob_no_shared = 1.0
    for i in range(num_people):
        prob_no_shared *= (months_in_year - i) / months_in_year

    # Probability of at least one shared month
    return 1 - prob_no_shared

def probability_same_birthday(num_people, days_in_year=365):

    if num_people > days_in_year:
        return 1.0  # If more people than days, there must be a match.

    # Calculate the probability that no one shares a birthday.
    prob_no_shared = 1.0
    for i in range(num_people):
        prob_no_shared *= (days_in_year - i) / days_in_year

    # Probability of at least one shared birthday
    return 1 - prob_no_shared


def main():
    parser = argparse.ArgumentParser(description="Calculate the probability of shared birthdays, weekdays, or months.")
    parser.add_argument("num_people", type=int, help="Number of people to consider.")
    parser.add_argument("--days_in_year", type=int, default=365, help="Number of days in a year (default: 365).")
    parser.add_argument("--days_in_week", type=int, default=7, help="Number of days in a week (default: 7).")
    parser.add_argument("--months_in_year", type=int, default=12, help="Number of months in a year (default: 12).")

    args = parser.parse_args()

    num_people = args.num_people
    days_in_year = args.days_in_year
    days_in_week = args.days_in_week
    months_in_year = args.months_in_year

    prob_weekday = probability_same_weekday(num_people, days_in_week)
    prob_month = probability_same_month(num_people, months_in_year)
    prob_birthday = probability_same_birthday(num_people, days_in_year)

    print(f"Probability of at least two people sharing the same day of the week among {num_people} people: {prob_weekday:.6f}")
    print(f"That is approximately {prob_weekday * 100:.2f}% chance.")

    print(f"Probability of at least two people sharing the same month of birth among {num_people} people: {prob_month:.6f}")
    print(f"That is approximately {prob_month * 100:.2f}% chance.")

    print(f"Probability of at least two people sharing the same birthday among {num_people} people: {prob_birthday:.6f}")
    print(f"That is approximately {prob_birthday * 100:.2f}% chance.")

 
if __name__ == "__main__":
    main()

