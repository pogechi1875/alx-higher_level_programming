#!/usr/bin/python3

""" initialise the class"""


class Square:
    """Creating an instantiation of the class Square"""
    def __init__(self, size=0):

        self.__size = size

        if isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0 ")
