#!/usr/bin/python3
# File name:
#       102-magic_calculation.py
# Description:
#       Matches the bytecode seen in
#       the README.
# Author:
#       eu-dk3-t


def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    return sub(a, b)
