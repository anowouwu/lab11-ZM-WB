"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b): 
    pass

import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    try:
        return math.log(b, a)# use math library + raise ValueError
    except ValueError as e:
        raise ValueError

def exp(a, b):
    return a**b

import math

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def logarithm(a, b):
    try: return math.log(a, b)
    except ValueError: print("Value error.")
def exponent(a, b):
    return a**b
