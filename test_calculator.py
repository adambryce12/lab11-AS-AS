#https://github.com/adambryce12/lab11-AS-AS.git 
import unittest
import calculator
import math

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(3, 5), 8)
        self.assertEqual(calculator.add(-1, 4), 3)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 3), 7)
        self.assertEqual(calculator.subtract(0, 5), -5)
        self.assertEqual(calculator.subtract(-2, -2), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 5)

    def test_logarithm(self):
        self.assertEqual(calculator.logarithm(2, 8), 3)
        self.assertEqual(calculator.logarithm(10, 100), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, 0)


if __name__ == "__main__":
    unittest.main()
