#!/usr/bin/python3
# File name:
#       7-update_dictionary.py
# Description:
#       Updates and Returns a new cp of a list
# Author:
#       eu-dk3-t


def update_dictionary(a_dictionary, key, value):
    a_dictionary.update({key: value})
    return (a_dictionary.copy())
