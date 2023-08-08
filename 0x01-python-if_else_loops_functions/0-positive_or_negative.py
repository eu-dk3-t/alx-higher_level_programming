#!/usr/bin/python3
# File name:
#       0-positive_or_negative.py
# Description:
#       Generates a random number
#       assesses its polarity
# Author:
#       eu-dk3-t

import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number:d} is positive")
elif number == 0:
    print(f"{number:d} is zero")
else:
    print(f"{number:d} is negative")
