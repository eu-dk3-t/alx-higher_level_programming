#!/usr/bin/python3
""" Module containing the `Square` class
that inherits the `Rectangle` class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Inherits the `Rectangle` class. """

    def __init__(self, size):
        """
        Initializes the `Square` instance.
        Args:
            size (int): `size` of the `Square` instance.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ STring Representation """
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
