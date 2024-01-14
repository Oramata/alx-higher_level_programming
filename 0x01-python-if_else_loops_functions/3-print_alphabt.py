#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

alphabet = ""

for i in range(97, 123):
    if chr(i) not in ['q', 'e']:
        alphabet += chr(i)

print("{}".format(alphabet))
