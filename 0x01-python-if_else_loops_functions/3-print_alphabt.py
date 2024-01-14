#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

for i in range(97, 123):
    if chr(i) not in ['q', 'e']:
        print("{}".format(chr(i)), end='')
