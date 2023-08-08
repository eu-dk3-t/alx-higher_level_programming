#!/usr/bin/python3
# File name:
#       1-last_digit.py
# Description:
#       Generates a random number and
#       prints its final digit
# Author:
#       eu-dk3-t


import random
number = random.randint(-10000, 10000)

# check for negative numbbers
if number < 0:
    lastDigit = -((-1*number) % 10)
else:
    lastDigit = number % 10

# check the last digit of the number
if lastDigit == 0:
    print(f"Last digit of {number:d} is {lastDigit:d} and is 0")
elif lastDigit > 5:
    print(f"Last digit of {number:d} is {lastDigit:d} and is greater\
 than 5")
elif lastDigit < 6 and lastDigit != 0:
    print(f"Last digit of {number:d} is {lastDigit:d} and is\
 less than 6 and not 0")
