#!/usr/bin/python3

import sys  # Import the sys module to access command-line arguments

if __name__ == "__main__":
    infinite_add = 0
    args = sys.argv[1:]
    for element in args:
        number = int(element)
        infinite_add += number
    print(infinite_add)
