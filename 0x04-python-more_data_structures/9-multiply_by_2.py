#!/usr/bin/python3
# File name:
#       9-multiply_by_2.py
# Description:
#       Returns a new dict with all values
#       multiplied by 2
# Author:
#       eu-dk3-t


def multiply_by_2(a_dictionary):
    return ({pos: a_dictionary[pos] * 2 for pos in a_dictionary})
