#!/usr/bin/python3

"""Initiallise the class"""

class Square:
	def __init__(self, size=0):
		self.__size = size
		if not type(size) is int:
			raise TypeError("Size must be an intager")
		if size < 0 :
			raise ValueError("size must be >= 0")
