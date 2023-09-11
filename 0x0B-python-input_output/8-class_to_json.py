#!/usr/bin/python3
"""
Returns dict description with simple structure
for JSON Serialization of an object.
"""


def class_to_json(obj):
    """ Creates a json representation of an object. """
    return obj.__dict__
