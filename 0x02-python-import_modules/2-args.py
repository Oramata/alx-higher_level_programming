#!/usr/bin/python3

import sys

def print_arguments(argv):
    num_args = len(argv) - 1  # Subtract 1 to exclude the script name
    if num_args == 0:
        print("Number of argument(s): 0.")
    else:
        if num_args == 1:
            print("Number of argument: 1 argument:")
        else:
            print(f"Number of arguments: {num_args} arguments:")

        for i in range(1, len(argv)):
            print(f"{i}: {argv[i]}")

if __name__ == "__main__":
    print_arguments(sys.argv)