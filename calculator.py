"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b): return a + b
def mul(a, b): return a * b
def div(a, b):
        if a == 0:
            raise ZeroDivisionError
        return b / a
def exp(a, b): return a**b
def square_root(a):
    try: return math.sqrt(a)
    except ValueError: print("a < 0 value error")
def hypotenuse(a, b):
    return math.hypot(a, b)
def subtract(a, b):
    return a - b
def logarithm(a, b):
    try: return math.log(a, b)
    except ValueError: print("Value error.")