# tests/test_factorial.py

"""
Unit tests for the calculate_factorial function.
Author: Melat Assefa
Date: January 6, 2025
"""

import unittest
from solutions.calculate_factorial import calculate_factorial


class TestCalculateFactorial(unittest.TestCase):
    """Test cases for the calculate_factorial function."""

    def test_factorial_of_positive_number(self):
        """Test that the function returns correct factorial for a positive number."""
        self.assertEqual(calculate_factorial(5), 120)

    def test_factorial_of_zero(self):
        """Test that the function returns 1 for 0."""
        self.assertEqual(calculate_factorial(0), 1)

    def test_factorial_of_one(self):
        """Test that the function returns 1 for 1."""
        self.assertEqual(calculate_factorial(1), 1)

    def test_negative_input(self):
        """Test that the function raises an error for negative input."""
        with self.assertRaises(ValueError):
            calculate_factorial(-1)


if __name__ == "__main__":
    unittest.main()
