#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """ Class Square """
    def __init__(self, size=0, position=(0, 0)):
        """
        Function name:
            __init__
        Description:
            Initialization
        """
        if self.__validate_size(size):
            self.__size = size
        if self.__validate_position(position):
            self.__position = position

    @property
    def size(self):
        """
        Function name:
            size
        Description:
            getter for size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Function name:
            size
        Description:
            setter for size attribute
        """
        if self.__validate_size(value):
            self.__size = value

    @property
    def position(self):
        """
        Function name:
            position
        Description:
            getter for position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Function name:
            position
        Description:
            setter for position attribute
        """
        if self.__validate_position(value):
            self.__position = value

    def area(self):
        """
        Function name:
            area
        Description:
            Calculates the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Function name:
            prints the square using '#' characters
            takes (x, y) offsets into account
        """
        i = 0
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__position[1]):
            print()
        i = 0
        for i in range(0, self.__size):
            j = 0
            x_pad = 0
            for x_pad in range(0, self.__position[0]):
                print(" ", end='')
            for j in range(0, self.__size):
                print("#", end='')
            print()

    def __validate_size(self, size):
        """
        Function name:
            __validate_size
        Description:
            Validates the size
            Checks for errors
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False

    def __validate_position(self, position):
        """
        Function name:
            __validate_position
        Function name:
            Validates the position
            Checks for type errors
        """
        if not isinstance(position, type((0, 0))):
            raise TypeError("position must be a tuple of 2 positive integers")
            return False
        return True
