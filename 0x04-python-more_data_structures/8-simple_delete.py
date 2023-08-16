#!/usr/bin/python3
# File name:
#       8-simple_delete.py
# Description:
#       Deletes an element based on the key from a dict
# Author:
#       eu-dk3-t


def simple_delete(a_dictionary, key=""):
    if key is not "" and key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary.copy())
