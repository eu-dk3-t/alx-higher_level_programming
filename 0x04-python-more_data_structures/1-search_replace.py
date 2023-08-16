#!/usr/bin/python3
# File name:
#       1-search_replace.py
# Description:
#       Searches for an item and
#       replaces it
# Author:
#       eu-dk3-t


def search_replace(my_list, search, replace):
    return ([item if item != search else replace for item in my_list])
