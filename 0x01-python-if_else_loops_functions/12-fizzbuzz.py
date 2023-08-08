#!/usr/bin/python3
# File name:
#       12-fizzbuzz.py
# Description:
#       Prints Fizz for multiples
#       of 3 and Buzz for mulriples of 5.
# Author:
#       eu-dk3-t


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        else:
            print("{:d}".format(i), end=" ")
