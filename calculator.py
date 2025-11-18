#https://github.com/adambryce12/lab11-AS-AS.git 
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Invalid base")
    if b <= 0:
        raise ValueError("Invalid number")
    return math.log(b, a)

def exponent(a, b):
    return a ** b

def hypotenuse(a, b):
    return math.sqrt(a*a + b*b)

def square_root(a):
    if a < 0:
        raise ValueError("Negative number")
    return math.sqrt(a)
