#!/usr/bin/python3
# File name:
#       1-element_at.py
# Description:
#       Retrieves an element from a list
# Author:
#       eu-dk3-t


def element_at(my_list, idx):
     if idx < 0 or idx > (len(my_list)):
        return None
    return (my_list[idx])
