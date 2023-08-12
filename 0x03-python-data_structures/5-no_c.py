#!/usr/bin/python3
# File name:
#       5-no_c.py
# Description:
#       Remove all 'C' letters
#       from a string
# Author:
#       eu-dk3-t


def no_c(my_string):
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
