# -*- coding: utf-8 -*-
"""
@author: Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand.
Print out and also save, Pascal's Triangle. 

Last updated: 7 June 2023

How to run:
python ./pascal-triangle.py -h
python ./pascal-triangle.py 5 standard out.txt
python ./pascal-triangle.py 5 hypercubes out.txt

Reference: https://en.wikipedia.org/wiki/Pascal%27s_triangle
"""

import argparse

def generate_pascal(n, type):
    triangle = [[1] * i for i in range(1, n + 2)]
    for i in range(2, n + 1):
        for j in range(1, i):
            if type == "hypercubes":
                triangle[i][j] = 2 * triangle[i - 1][j - 1] + triangle[i - 1][j]
            else:  # standard
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle

def print_pascal(triangle):
    n = len(triangle)
    for i in range(n):
        print(' ' * (n - i), end='')
        print('   '.join(str(j) for j in triangle[i]))
        
def write_pascal_to_file(triangle, file_name):
    with open(file_name, 'w') as f:
        n = len(triangle)
        for i in range(n):
            f.write(' ' * (n - i))
            f.write('   '.join(str(j) for j in triangle[i]))
            f.write('\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="Number of rows for Pascal's Triangle", type=int)
    parser.add_argument("type", help="Type of Pascal's Triangle (standard, hypercubes)", type=str)
    parser.add_argument("file_name", help="Name of the file to save the triangle", type=str)
    args = parser.parse_args()

    triangle = generate_pascal(args.n, args.type)
    print_pascal(triangle)
    write_pascal_to_file(triangle, args.file_name)
