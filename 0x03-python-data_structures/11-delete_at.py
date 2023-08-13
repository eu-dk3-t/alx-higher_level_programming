#!/usr/bin/python3
# File name:
#      11-delete_at.py
# Description:
#       Deletes an item at a specified idx
# Author:
#       eu-dk3-t


def delete_at(my_list=[], idx=0):
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
