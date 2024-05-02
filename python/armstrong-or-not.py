"""
Playing with Armstrong numbers.
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Last updated: 2 May 2024.

Usage:

(base) ye@lst-gpu-server-197:~/tmp$ python ./armstrong-or-not.py 100
100 is not an Armstrong number.
The closest Armstrong number is 153.

(base) ye@lst-gpu-server-197:~/tmp$ python ./armstrong-or-not.py 153
153 is an Armstrong number.
Calculation: 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
"""

import sys

def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    total = sum(int(digit) ** num_digits for digit in num_str)
    return total == num

def closest_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    closest = None
    min_diff = float('inf')
    for i in range(10 ** (num_digits - 1), 10 ** num_digits):
        if is_armstrong_number(i):
            diff = abs(num - i)
            if diff < min_diff:
                closest = i
                min_diff = diff
    return closest

def armstrong_calculation(num):
    num_str = str(num)
    num_digits = len(num_str)
    calculation = " + ".join([f"{digit}^{num_digits}" for digit in num_str])
    total = sum(int(digit) ** num_digits for digit in num_str)
    intermediate_steps = " + ".join([f"{int(digit) ** num_digits}" for digit in num_str])
    return f"{calculation} = {intermediate_steps} = {total}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python armstrong.py <number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Please enter a valid integer.")
        sys.exit(1)

    if number < 0:
        print("Please enter a non-negative number.")
        sys.exit(1)

    if is_armstrong_number(number):
        calculation = armstrong_calculation(number)
        print(f"{number} is an Armstrong number.")
        print(f"Calculation: {calculation}")
    else:
        closest = closest_armstrong_number(number)
        if closest:
            print(f"{number} is not an Armstrong number.")
            print(f"The closest Armstrong number is {closest}.")
        else:
            print(f"{number} is not an Armstrong number.")
            print("There are no Armstrong numbers with the same number of digits.")
