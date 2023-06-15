#!/usr/bin/python3
""" A class that defines a square by its size"""


class Square:
    "This is a Square"""
    pass

    def __init__(self, size=0):
        """ Method to initialize the square object.
Args size(int): The size """
        self.__size = size
        self.__validate_size()

    def __validate_size(self):
        """Validates the size.

        Raises:
            TypeError: if the size is not integer.
            TypeValue: if the size is less than 0."""
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Method that returns the area of a square.
        """
        return (self.__size * self.__size)
