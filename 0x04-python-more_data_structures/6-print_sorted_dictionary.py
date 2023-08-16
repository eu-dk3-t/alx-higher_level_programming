#!/usr/bin/python3
# File name:
#       6-print_sorted_dictionary.py
# Description:
#       Prints a dict by ordered keys
# Author:
#       eu-dk3-t


def print_sorted_dictionary(a_dictionary):
    [print(f"{key}: {a_dictionary[key]}") for key in sorted(a_dictionary)]

