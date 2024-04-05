#!/usr/bin/python3
try:
    Number = int(input("Enter a number: "))
    print(f"{Number} Battery street ")
except ValueError:
    raise ValueError("Invalid input: Please enter a valid number")

