"""
Module represents unit test for fizzbuzz_challenge

Created on 01/05/2024
Author Svitlana Musiienko
"""

import unittest

from ..fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    """Test the fizzbuzz function"""

    def test_fizz(self):
        """Check the numbers which are devisable by 3"""
        actual = fizzbuzz(6)
        expected = [1, 2, "Fizz", 4, "Buzz", "Fizz"]
        self.assertEqual(actual, expected)

    def test_buzz(self):
        """Check the numbers which are devisable by 5"""
        actual = fizzbuzz(10)
        expected = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"]
        self.assertEqual(actual, expected)

    def test_fizzbuzz(self):
        """Check the numbers which are devisable both by 3 and 5"""
        actual = fizzbuzz(15)
        expected = [
            1,
            2,
            "Fizz",
            4,
            "Buzz",
            "Fizz",
            7,
            8,
            "Fizz",
            "Buzz",
            11,
            "Fizz",
            13,
            14,
            "FizzBuzz",
        ]
        self.assertEqual(actual, expected)

    def test_other(self):
        """Check the numbers which are not devisable by 3 or 5 or both"""
        actual = fizzbuzz(2)
        expected = [
            1,
            2,
        ]
        self.assertEqual(actual, expected)

    def test_less_than_0(self):
        """Check the assertion error if the numbers less than 0"""
        with self.assertRaises(AssertionError):
            fizzbuzz(-1)

    def test_not_an_integer(self):
        """Check the assertion error if the argument is not integer"""
        with self.assertRaises(AssertionError):
            fizzbuzz(2.0)


if __name__ == "__main__":
    unittest.main()
