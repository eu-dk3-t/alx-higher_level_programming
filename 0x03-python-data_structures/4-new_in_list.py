#!/usr/bin/python3
# File name:
#       4-new_in_list.py
# Description:
#      Replaces an element in a
#       copied list at a specified
#       position
# Author:
#       eu-dk3-t


def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    copy = [x for x in my_list]
    copy[idx] = element
    return (copy)
