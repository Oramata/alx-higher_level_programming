#!/usr/bin/env python3

def magic_calculation(a, b):
    return 98 + a ** b

# Testing the function
print(magic_calculation(2, 3))  # Should output 98 + 2**3 = 106
print(magic_calculation(1, 1))  # Should output 98 + 1**1 = 99
print(magic_calculation(0, 0))  # Should output 98 + 0**0 = 99 (as 0**0 is 1)
