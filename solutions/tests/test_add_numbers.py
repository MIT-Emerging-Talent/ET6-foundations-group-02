# tests/test_add_two_numbers.py

"""
Unit tests for the add_two_numbers function.
This test suite includes:
- Regular cases: Typical inputs that the function is expected to handle.
- Edge cases: Inputs that are at the boundary of what the function should handle.
- Error cases: Inputs that should raise exception due to invalid input.

Created on: January 6, 2025
@author: Melat Assefa
"""

import unittest
from solutions.add_numbers import add_numbers


class TestAddNumbers(unittest.TestCase):
    """Unit tests for the add_numbers function."""

    # Regular Cases
    def test_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(add_numbers(2, 3), 5)

    def test_negative_numbers(self):
        """Test adding two negative numbers."""
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_mixed_sign_numbers(self):
        """Test adding a positive and a negative number."""
        self.assertEqual(add_numbers(-1, 1), 0)

    def test_floats(self):
        """Test adding two floating-point numbers."""
        self.assertEqual(add_numbers(0.5, 0.5), 1.0)

    # Edge Cases
    def test_add_zero_to_number(self):
        """Test adding zero to a number."""
        self.assertEqual(add_numbers(0, 5), 5)

    def test_add_number_to_zero(self):
        """Test adding a number to zero."""
        self.assertEqual(add_numbers(5, 0), 5)

    def test_large_numbers(self):
        """Test adding very large numbers."""
        self.assertEqual(add_numbers(1e308, 1e308), 2e308)

    # Defensive Cases
    def test_type_error_with_string_first(self):
        """Test that a TypeError is raised for non-numeric input as first argument."""
        with self.assertRaises(TypeError):
            add_numbers("a", 1)

    def test_type_error_with_string_second(self):
        """Test that a TypeError is raised for non-numeric input as second argument."""
        with self.assertRaises(TypeError):
            add_numbers(1, "b")


if __name__ == "__main__":
    unittest.main()
