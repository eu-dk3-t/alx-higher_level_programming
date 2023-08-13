#!/usr/bin/python3
# File name:
#      9-max_integer.py
# Description:
#       Find the biggest int in a list
# Author:
#       eu-dk3-t


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    biggest = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > biggest:
            biggest = my_list[i]

    return (biggest)
