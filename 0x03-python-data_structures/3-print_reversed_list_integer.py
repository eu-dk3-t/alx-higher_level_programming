#!/usr/bin/python3
# File name:
#       3-print_reversed_list_integer.py
# Description:
#   Prints all integers in a list in reverse
# Author:
#       eu-dk3-t


def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
