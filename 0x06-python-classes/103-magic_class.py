#!/usr/bin/python3
"""MagicClass"""


import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """
        Function nameL
            __init__
        Description:
            Initialization
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Function name:
            area
        Description:
                Return the area of the MagicClass, circle
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Function name:
            circumference
        Description:
                Return The circumference of the MagicClass, circle
        """
        return (2 * math.pi * self.__radius)
