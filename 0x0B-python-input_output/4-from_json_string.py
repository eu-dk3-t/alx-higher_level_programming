#!/usr/bin/python3
""" Deserializes JSON data to py objs. """
from json import loads as ld


def from_json_string(my_str):
    """ Deserializes a JSON string back to a python object. """
    return ld(my_str)
