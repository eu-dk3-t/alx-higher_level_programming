#!/usr/bin/python3
""" Module containing the `BaseGeometry` class. """


class BaseGeometry:
    """ Base Geometry Class """

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if value is an integer and if it is > 0."""
        """
        Args:
            name (:obj:'str'): String.
            value (int): An integer.
        """

        if type(value) !=  int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
