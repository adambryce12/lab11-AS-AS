https://github.com/adambryce12/lab11-AS-AS.git 
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    import calculator
import pytest
import math

def test_add():
    assert calculator.add(3, 5) == 8
    assert calculator.add(-1, 4) == 3
    assert calculator.add(0, 0) == 0

def test_subtract():
    assert calculator.sub(10, 3) == 7
    assert calculator.sub(0, 5) == -5
    assert calculator.sub(-2, -2) == 0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.div(0, 5)

def test_logarithm():
    assert calculator.log(2, 8) == 3
    assert calculator.log(10, 100) == 2

def test_log_invalid_base():
    with pytest.raises(ValueError):
        calculator.log(1, 10)
    with pytest.raises(ValueError):
        calculator.log(-2, 10)
    with pytest.raises(ValueError):
        calculator.log(2, 0)

if __name__ == "__main__":
    unittest.main()
