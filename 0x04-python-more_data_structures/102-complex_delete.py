#!/usr/bin/python3
# File name:
#       102-complex_delete.py
# Description:
#       Deletes keys with specific values
# Author:
#       eu-dk3-t


def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict):
        item = list(k for k in a_dictionary.keys() if a_dictionary[k]
                     is value)
        for k in item:
                del a_dictionary[k]
        return a_dictionary
