#!/usr/bin/python3
""" Loads data from JSON files. """
from json import loads as ld


def load_from_json_file(filename):
    """ Loads an object from json file. """
    with open(filename, encoding='utf-8') as myFile:
        return (ld(myFile.read()))
