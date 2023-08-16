#!/usr/bin/python3
# File name:
#       12-roman_to_int.py
# Description:
#       Converts Roman numbers to integers
# Author:
#       eu-dk3-t


def roman_to_int(roman_string):
    romanN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_num = 0
    for i in range(len(roman_string)):
        if i > 0 and romanN[roman_string[i]] > romanN[roman_string[i - 1]]:
            int_num += romanN[roman_string[i]] - 2*romanN[roman_string[i - 1]]
        else:
            int_num += romanN[roman_string[i]]
    return int_num
