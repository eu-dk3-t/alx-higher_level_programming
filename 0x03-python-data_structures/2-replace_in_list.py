#!/usr/bin/python3
# File name:
#       2-replace_in_list.py
# Description:
#       Replaces an element at a speccified position
# Author:
#       eu-dk3-t


def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
