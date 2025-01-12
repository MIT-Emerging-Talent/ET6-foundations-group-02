# tests/test_prime_numbers.py

"""
Unit tests for the get_prime_numbers function.
This test suite includes:
- Regular cases: Typical inputs that the function is expected to handle.
- Edge cases: Inputs that are at the boundary of what the function should handle.
- Error cases: Inputs that should raise exception due to invalid input.

Created on: January 6, 2025
@author: Melat Assefa
"""

import unittest
from solutions.get_prime_numbers import get_prime_numbers


class TestGetPrimeNumbers(unittest.TestCase):
    """Test cases for the get_prime_numbers function."""

    # Regular Cases
    def test_primes_up_to_10(self):
        """Regular case: Test that the function returns correct primes up to 10."""
        self.assertEqual(get_prime_numbers(10), [2, 3, 5, 7])

    def test_primes_up_to_2(self):
        """Regular case: Test that the function returns correct primes up to 2."""
        self.assertEqual(get_prime_numbers(2), [2])

    # Edge Cases
    def test_no_primes_below_2_for_1(self):
        """Edge case: Test that the function returns an empty list for n = 1."""
        self.assertEqual(get_prime_numbers(1), [])

    def test_no_primes_below_2_for_0(self):
        """Edge case: Test that the function returns an empty list for n = 0."""
        self.assertEqual(get_prime_numbers(0), [])

    def test_no_primes_below_2_for_negative(self):
        """Edge case: Test that the function returns an empty list for negative n."""
        self.assertEqual(get_prime_numbers(-5), [])

    def test_large_number(self):
        """Edge case: Test the function with a larger number."""
        self.assertEqual(get_prime_numbers(20), [2, 3, 5, 7, 11, 13, 17, 19])

    # Error Cases
    def test_non_integer_input_raises_type_error(self):
        """Error case: Test that the function raises a TypeError for non-integer input."""
        with self.assertRaises(TypeError):
            get_prime_numbers("ten")
        with self.assertRaises(TypeError):
            get_prime_numbers(5.5)
        with self.assertRaises(TypeError):
            get_prime_numbers(None)


if __name__ == "__main__":
    unittest.main()
