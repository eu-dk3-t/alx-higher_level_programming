#!/usr/bin/python3
# File name:
#       2-uniq_add.py
# Description:
#       Adds all unique elements
#       of a list of ints together
# Author:
#       eu-dk3-t


def uniq_add(my_list=[]):
    return (sum({item for item in my_list}))
