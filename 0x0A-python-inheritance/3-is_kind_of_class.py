#!/usr/bin/python3
""" Module containing the `is_kind_of_class` function. """


def is_kind_of_class(obj, a_class):
    """
    Check if `obj` is an instance of a
    `a_class` or a child class that
    inherits from it.
    Args:
        obj: An object.
        a_class: A class.
    Returns: True if ` isinstance a `a_class`, False if not.
    """
    return isinstance(obj, a_class)
