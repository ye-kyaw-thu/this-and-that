# Written by Ye, LU Lab., Myanmar
# Last updated: 27 Sept 2023
# Demo of applying Turing Machine concept for detecting Padsints
# How to run:
# e.g.

import sys
import argparse

class PadsintTuringMachine:
    def __init__(self, input_file):
        self.state = 'START'
        self.buffer = []
        self.subscripts = [] # List to collect found subscript consonants
        self.input_file = input_file

    def process_char(self, char):
        # START state: Normal reading until we find a subscript marker
        if self.state == 'START':
            if char == '္':
                self.state = 'FOUND_SUBSCRIPT'
            else:
                self.buffer.append(char)
        # FOUND_SUBSCRIPT state: When we detect a subscript marker, we process the next char
        elif self.state == 'FOUND_SUBSCRIPT':
            if char != '\n' and len(self.buffer) > 0:
                stacked_syllable = f"{self.buffer[-1]}္{char}"
                self.subscripts.append(stacked_syllable)
            self.state = 'START'

    def process_file(self):
        with open(self.input_file, 'r', encoding='utf-8') as f:
            for line in f:
                for char in line:
                    self.process_char(char)
                if self.subscripts:
                    yield ', '.join(self.subscripts)
                self.buffer = []
                self.subscripts = []

def main():
    parser = argparse.ArgumentParser(description='Detect Burmese subscript combinations or Padsints in a file.')
    parser.add_argument('input_file', help='Input file containing Burmese text')
    parser.add_argument('-o', '--output_filename', help='Output file to save results. If not provided, results are printed to the console.', default=None)

    args = parser.parse_args()

    tm = PadsintTuringMachine(args.input_file)
    results = tm.process_file()

    if args.output_filename:
        with open(args.output_filename, 'w', encoding='utf-8') as f:
            for line in results:
                f.write(line + '\n')
    else:
        for line in results:
            print(line)

if __name__ == '__main__':
    main()
