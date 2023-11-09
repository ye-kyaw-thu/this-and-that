## Written by Ye Kyaw Thu, LU Lab., Myanmar
## The formula for the sum of an arithmetic progression or arithmetic series
## Last updated: 10 Nov 2023

import sys
import time

def gauss_sum(start, end):
    """Calculate the sum of an arithmetic series using Gauss' method.
    Complexity: O(1)"""
    return (end - start + 1) * (start + end) // 2

def sequential_sum(start, end):
    """Calculate the sum by sequentially adding each number.
    Complexity: O(n)"""
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

def main(start, end):
    # Convert string arguments to integers
    start = int(start)
    end = int(end)

    # Time and execute Gauss' method
    start_time = time.time()
    gauss_result = gauss_sum(start, end)
    gauss_time = time.time() - start_time

    # Time and execute the sequential method
    start_time = time.time()
    sequential_result = sequential_sum(start, end)
    sequential_time = time.time() - start_time

    print(f"Gauss Method: Sum = {gauss_result}, Time = {gauss_time:.6f} seconds, Complexity: O(1)")
    print(f"Sequential Method: Sum = {sequential_result}, Time = {sequential_time:.6f} seconds, Complexity: O(n)")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sum_comparison.py <start_number> <end_number>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
