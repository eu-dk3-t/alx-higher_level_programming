#!/usr/bin/python3
""" Return JSON rep of string """
from json import dumps as dp


def to_json_string(my_obj):
    """ Returns json string containing object's representation """
    return dp(my_obj)
