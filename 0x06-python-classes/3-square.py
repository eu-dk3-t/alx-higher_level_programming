#!/usr/bin/python3


class Square:
    """ class square with attribute size """
    def __init__(self, size=0):
        """
        Function name:
            __init__
        Description:
            Checks for errors
            Initialization
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Function name:
            area
        Description:
            Calculates the area of the square
        """
        return self.__size ** 2
