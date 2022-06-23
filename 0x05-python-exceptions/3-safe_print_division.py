#!/usr/bin/python3
def safe_print_division(a, b):
    diffrence = None

    try:
        diffrence = a / b
    except ZeroDivisionError:
        return diffrence
    finally:
        print("Inside result: {}".format(diffrence))
