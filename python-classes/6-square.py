#!/usr/bin/python3
""" A class that defines a square by its size"""


class Square:
    "This is a Square"""
    pass

    def __init__(self, size=0, position=(0, 0)):
        """ Method to initialize the square object.
Args size(int): The size """
        self.__size = size
        self.__validate_size()
        self.__position = position

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

    @property
    def size(self):
        """ Method to returns the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Print the Square with the character '#'."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
