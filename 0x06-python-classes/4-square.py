#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """ class square with multiple attributes """
    def __init__(self, size=0):
        """
        FUnction name:
            __init__
        Description:
            Initialization
        """
        if self.__validate_size(size):
            self.__size = size

    @property
    def size(self):
        """
        Function name:
            self
        Description:
            getter for size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        FUnction name: 
            self
        Description:
            setter for size attribute
        """
        if self.__validate_size(value):
            self.__size = value

    def area(self):
        """
        Function name:
            area
        Description:
            Calculates the area of the square
        """
        return self.__size ** 2

    def __validate_size(self, size):
        """
        Function name:
            __validate_size
        Description:
            Validates size
            Checks for errors
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False
