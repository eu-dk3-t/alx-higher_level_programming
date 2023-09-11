#!/usr/bin/python3


def is_same_class(obj, a_class):
    """
    Checks if two objects are EXACTLY the same class
    """
    if type(obj) != a_class:
        return False
    return True
