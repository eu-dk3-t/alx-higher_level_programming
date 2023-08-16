#!/usr/bin/python3
# File name:
#       100-weight_average.py
# Description:
#       Returns the weighted average of all
#       ints in a list of tuples
# Author:
#       eu-dk3-t


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total = 0
    quantity = 0
    for struct in my_list:
        total += (struct[0] * struct[1])
        quantity += struct[1]
    return (total/quantity)
