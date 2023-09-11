#!/usr/bin/python3
""" Module containing the `MyInt` class """


class MyInt(int):
    """ Inherits the `int` class """
    def __eq__(self, other):
        """
        Overrides equality operator
        Calls inequality operator
        Args:
            other (int): An int.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides inequality operator
        Calls equality operator
        Args:
            other (int): An int.
        """
        return super().__eq__(other)
