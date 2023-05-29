# -*- coding: utf-8 -*-
"""
Created on Sat May 29 10:17:03 2023

@author: Ye Kyaw Thu, Study on Prime Number Calculations with ChatGPT4
How to run: python print-prime-no.py 10 100

"""

import argparse
import math
import time
import numpy

def brute_force(start, end):
    def is_prime(num):
        if num <= 1:
            return False
        for divisor in range(2, num):
            if num % divisor == 0:
                return False
        return True

    return [num for num in range(start, end + 1) if is_prime(num)]

def trial_division(start, end):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False

        sqr = math.isqrt(num) + 1
        for divisor in range(3, sqr, 2):
            if num % divisor == 0:
                return False
        return True

    return [num for num in range(start, end + 1) if is_prime(num)]

def sieve_of_eratosthenes(start, end):
    sieve = [True] * (end + 1)
    for num in range(2, math.isqrt(end) + 1):
        if sieve[num]:
            for multiple in range(num*num, end + 1, num):
                sieve[multiple] = False
    return [num for num in range(max(start, 2), end + 1) if sieve[num]]

def optimized_trial_division(start, end):
    def is_prime(num):
        if num < 2:
            return False
        if num == 2 or num == 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False

        i = 5
        w = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    return [num for num in range(start, end + 1) if is_prime(num)]

def sieve_of_sundaram(start, end):
    n = end // 2
    sieve = [False] * (n + 1)
    
    for x in range(1, n + 1):
        for y in range(1, (n - x) // (2 * x + 1) + 1):
            sieve[x + y + 2 * x * y] = True

    if start <= 2:
        yield 2
    for x in range(1, n + 1):
        if not sieve[x]:
            p = 2 * x + 1
            if p >= start:
                yield p

def sieve_of_atkin(start, end):
    sieve = [False] * (end + 1)
    sqrtn = int(end ** 0.5)
    
    x_max = int((sqrtn / 2)**0.5) + 1
    for xd in range(1, x_max):
        x = 4 * xd**2
        for t in range(0, 2 * xd + 1):
            if x + t <= end:
                sieve[x + t] = not sieve[x + t]
            if x + t - 2 * xd <= end and t > 2 * xd:
                sieve[x + t - 2 * xd] = not sieve[x + t - 2 * xd]

    y_max = int((sqrtn - 1) / 2) + 1
    for yd in range(1, y_max):
        y = 3 * yd**2
        for t in range(0, 2 * yd + 1):
            if y + t <= end:
                sieve[y + t] = not sieve[y + t]
            if y + t - 2 * yd <= end and t > 2 * yd:
                sieve[y + t - 2 * yd] = not sieve[y + t - 2 * yd]

    i_max = sqrtn + 1
    for i in range(5, i_max):
        if sieve[i]:
            i2 = i * i
            for j in range(i2, end + 1, i2):
                sieve[j] = False
                
    return [p for p in range(max(2, start), end + 1) if sieve[p]]

def segmented_sieve(start, end):
    def simple_sieve(limit, primes):
        mark = [True for _ in range(limit + 1)]
        p = 2
        while p * p <= limit:
            if mark[p] is True:
                for i in range(p * p, limit + 1, p):
                    mark[i] = False
            p += 1
        for p in range(2, limit):
            if mark[p]:
                primes.append(p)
    
    def segmented_sieve_helper(low, high, primes):
        mark = [True for _ in range(high - low + 1)]
        for i in range(len(primes)):
            low_limit = (low // primes[i]) * primes[i]
            if low_limit < low:
                low_limit += primes[i]
            if low_limit == primes[i]:
                low_limit += primes[i]
            for j in range(low_limit, high + 1, primes[i]):
                mark[j - low] = False
        for i in range(low, high + 1):
            if mark[i - low]:
                yield i

    primes = []
    limit = math.isqrt(end) + 1
    simple_sieve(limit, primes)

    return [num for num in segmented_sieve_helper(max(start, limit), end, primes) if num >= start]

def main():
    parser = argparse.ArgumentParser(description="Find prime numbers in a given range using different methods.")
    parser.add_argument("start", type=int, help="Start of the range.")
    parser.add_argument("end", type=int, help="End of the range.")

    args = parser.parse_args()

    methods = [brute_force, trial_division, sieve_of_eratosthenes, optimized_trial_division, sieve_of_sundaram, sieve_of_atkin, segmented_sieve]
    method_names = ["Brute Force", "Trial Division", "Sieve of Eratosthenes", "Optimized Trial Division", "Sieve of Sundaram", "Sieve of Atkin", "Segmented Sieve of Eratosthenes"]

    for method, name in zip(methods, method_names):
        start_time = time.time()
        primes = list(method(args.start, args.end))
        end_time = time.time()
        print(f"Method: {name}")
        print(f"Primes: {primes}")
        print(f"Time taken: {end_time - start_time} seconds")
        print()

if __name__ == "__main__":
    main()
