#!/usr/bin/python3
try:
    number = '98'
    print(f"{number} Battery street")
except ValueError:
    raise ValueError("Unknown format code 'd' for object of type 'str'")
