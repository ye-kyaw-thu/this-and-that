# -*- coding: utf-8 -*-
"""
@author: Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand.
Print out and also save, Pascal's Triangle. 
The file format is SQLite database.
Last updated: 7 June 2023

How to run:
python ./pascal-triangle-sql.py -h
python ./pascal-triangle-sql.py 5 standard out.txt
python ./pascal-triangle-sql.py 5 hypercubes out.txt
"""

import argparse
import sqlite3

def generate_pascal(n, type):
    conn = sqlite3.connect('pascal.db')
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS PascalTriangle (
            Row INTEGER,
            Column INTEGER,
            Value TEXT,
            PRIMARY KEY(Row, Column)
        )
    ''')
    
    c.execute("INSERT OR IGNORE INTO PascalTriangle VALUES (0, 0, '1')")
    
    for i in range(1, n + 1):
        for j in range(i + 1):
            if j == 0 or j == i:
                value = 1
            else:
                c.execute("SELECT Value FROM PascalTriangle WHERE Row = ? AND Column = ?", (i - 1, j - 1))
                left_parent = int(c.fetchone()[0])
                
                c.execute("SELECT Value FROM PascalTriangle WHERE Row = ? AND Column = ?", (i - 1, j))
                right_parent = int(c.fetchone()[0])
                
                if type == "hypercubes":
                    value = 2 * left_parent + right_parent
                else:  # standard
                    value = left_parent + right_parent
            
            c.execute("INSERT OR IGNORE INTO PascalTriangle VALUES (?, ?, ?)", (i, j, str(value)))
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="Number of rows for Pascal's Triangle", type=int)
    parser.add_argument("type", help="Type of Pascal's Triangle (standard, hypercubes)", type=str)
    args = parser.parse_args()

    generate_pascal(args.n, args.type)
