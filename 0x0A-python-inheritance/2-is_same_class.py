#!/usr/bin/python3
""" Class-checking function """

def is_same_class(obj, a_class):
    """ Checks if two objects are EXACTLY the same class """

    """
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        isInstance - True
        Otherwise - False.
    """
    if type(obj) != a_class:
        return False
    return True
