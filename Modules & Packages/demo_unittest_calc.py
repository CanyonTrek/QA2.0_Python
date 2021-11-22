#! /usr/bin/python
# Author: DCameron, V1.0, email
# Description: This program will demonstrate another example of
# creating functions with DocStrings, parameter passing, return values.
"""
    Calculator program with Add, Divide and Multiply functionality.
"""
import unittest
from demo_calculator import add, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(7, add(4, 3))

    def test_multiply(self):
        self.assertEqual(12, multiply(4, 3))

    def test_divide(self):
        self.assertEqual('1.333', divide(4, 3))


if __name__ == "__main__":
    unittest.main()

