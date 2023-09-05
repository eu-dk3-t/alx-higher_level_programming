#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Class name:
        LockedClass
    Attribute:
        first_name (str): name
    Misc:
        Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
