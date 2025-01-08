# !/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
Author: Melat Assefa
Date: January 6, 2025
"""
import unittest
from ..get_even_numbers import get_even_numbers  # type: ignore


class TestGetEvenNumbers(unittest.TestCase):
    """Test cases for the filter_even_numbers function."""

    def test_even_numbers(self):
        """Test that the function returns only even numbers."""
        self.assertEqual(get_even_numbers([1, 2, 3, 4]), [2, 4])

    def test_empty_list(self):
        """Test that the function returns an empty list for an empty input."""
        self.assertEqual(get_even_numbers([]), [])

    def test_invalid_input(self):
        """Test that the function raises an error when input is not a list."""
        with self.assertRaises(TypeError):
            get_even_numbers("not a list")
