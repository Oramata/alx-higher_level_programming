#!/usr/bin/python3

import sys

def infinite_add(argv):
    total = sum(int(arg) for arg in argv[1:])  # Skip argv[0] as it's the script name
    print(total)

if __name__ == "__main__":
    infinite_add(sys.argv)