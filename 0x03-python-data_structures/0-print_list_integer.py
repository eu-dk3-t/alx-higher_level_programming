#!/usr/bin/python3
# File name:
#       0-print_list_integer.py
# Description:
#       Prints all ints in a list
# Author:
#       eu-dk3-t


def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
