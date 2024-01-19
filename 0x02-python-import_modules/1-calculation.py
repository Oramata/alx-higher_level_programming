#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    print("Add: {} + {} = {}".format(a, b, add(a, b)))
    print("Sub: {} - {} = {}".format(a, b, sub(a, b)))
    print("Mul: {} * {} = {}".format(a, b, mul(a, b)))
    print("Div: {} / {} = {}".format(a, b, div(a, b)))