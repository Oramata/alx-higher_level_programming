#!/usr/bin/python
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        print(char, end="")
    print()
