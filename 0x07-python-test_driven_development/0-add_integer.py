#!/usr/bin/python3
""" Adds two integers. """


def add_integer(a, b=98):
    """
    Function name:
        add_integer
    Description:
        Adds two integers and returns the result.
    Args:
        a (int): The first integer.
        b (int): The secodn integer.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
