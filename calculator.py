"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    a + b

def subtract(a, b):
    a - b

def multiply(a, b):
    a * b


def logarithm(a, b):
    if b <= 0 or a <= 0 or a == 1:
        raise ValueError
    math.log(b, a)# use math library/raise ValueError

def exponent(a, b):
    a^b


