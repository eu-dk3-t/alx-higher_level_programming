#!/usr/bin/python3
""" Writes json strings to files. """
from json import dumps as dp


def save_to_json_file(my_obj, filename):
    """ Saves obj to a file """
    with open(filename, 'w', encoding='utf-8') as myFile:
        return myFile.write(dp(my_obj))
