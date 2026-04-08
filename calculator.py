"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    try: return b / a
    except ZeroDivisionError: print("Zero division error.")
def logarithm(a, b):
    try: return math.log(a, b)
    except ValueError: print("Value error.")
def exponent(a, b):
    return a**b