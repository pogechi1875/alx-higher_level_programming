#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    print(f"{number} number is zero")
elif number > 0:
    print(f"{number} number is positive")
else:
    print(f"{number} number is negative")
