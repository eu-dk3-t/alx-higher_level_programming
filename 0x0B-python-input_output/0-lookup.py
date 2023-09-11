#!/usr/bin/python3
""" Module containing lookup function """


def lookup(obj):
    """
    Function name:
        lookup
    Description:
        Returns all available attributes and methods of an object
    Args:
        obj: An object

    Returns: A list of all available attribues and methods.
    """
    return dir(obj)
