# decimal_to_binary.py

"""
Unit tests for the convert_decimal_to_binary function.
This test suite includes:
- Regular cases: Typical inputs that the function is expected to handle.
- Edge cases: Inputs that are at the boundary of what the function should handle.
- Error cases: Input that should raise exceptions due to invalid input.

@author: Melat Assefa
Date: January 6, 2025 
"""

import unittest
from solutions.decimal_to_binary import convert_decimal_to_binary


class TestConvertDecimalToBinary(unittest.TestCase):
    """Test cases for the convert_decimal_to_binary function."""

    # Regular Cases
    def test_binary_of_zero(self):
        """Regular case: Test that the function returns '0' for input 0."""
        self.assertEqual(
            convert_decimal_to_binary(0),
            "0",
            "The binary representation of 0 should be '0'.",
        )

    def test_binary_of_five(self):
        """Regular case: Test that the function returns '101' for input 5."""
        self.assertEqual(
            convert_decimal_to_binary(5),
            "101",
            "The binary representation of 5 should be '101'.",
        )

    def test_binary_of_twenty_three(self):
        """Regular case: Test that the function returns '10111' for input 23."""
        self.assertEqual(
            convert_decimal_to_binary(23),
            "10111",
            "The binary representation of 23 should be '10111'.",
        )

    # Edge Cases
    def test_large_number(self):
        """Edge case: Test the function with a large number."""
        self.assertEqual(
            convert_decimal_to_binary(1023),
            "1111111111",
            "The binary representation of 1023 should be '1111111111'.",
        )

    # Error Cases
    def test_negative_input_raises_value_error(self):
        """Error case: Test that the function raises a ValueError for negative input."""
        with self.assertRaises(ValueError):
            convert_decimal_to_binary(-1)


if __name__ == "__main__":
    unittest.main()
