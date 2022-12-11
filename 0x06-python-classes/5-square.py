#!/usr/bin/python3

class Square:
	def __init__(self, size=0):
		self.size = size
	@property
	def size(self):
		return(self.__size)

	@size.setter
	def size(self, value):
		if not type(value) is int:
			raise TypeError("size must be an integer")
		if value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	def area(self):
		return(self.__size * self.__size)

	def my_print(self):
		size = self.__size
		if size == 0:
			print("")
		else:
			for x in range(size):
				print('#'*self.__size)
