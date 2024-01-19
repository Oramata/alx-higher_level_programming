#!/usr/bin/python

import hidden_4  # imports the hidden_4 file from the directory file"

def print_names():
    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)

if __name__ == "__main__":
    print_names()