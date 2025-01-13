#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit test module for checking palindromes.

Test categories:
    - Standard cases: correct inputs for words and numbers;
    - Edge cases;
    - Defensive tests: wrong input types, assertions;

Author: fevziismailsahin
Created: 01/11/2025
"""

import sys
import unittest
from io import StringIO

from ..check_palindromes import check_palindromes


class TestCheckPalindromes(unittest.TestCase):
    """Test suite for checking palindromes."""

    def setUp(self):
        """Set up the test environment."""
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        """Tear down the test environment."""
        sys.stdout = sys.__stdout__

    # Standard cases: correct inputs
    def test_standard_case_1(self):
        """Test with typical valid inputs for words and numbers."""
        check_palindromes(["Radar", "12321", "Hello", "1.232.1", "12345", "aA", "Test"])
        self.assertIn("'Radar' is a palindrome.", self.held_output.getvalue())
        self.assertIn("'12321' is a palindrome.", self.held_output.getvalue())
        self.assertIn("'Hello' is not a palindrome.", self.held_output.getvalue())
        self.assertIn("'1.232.1' is a palindrome.", self.held_output.getvalue())
        self.assertIn("'12345' is not a palindrome.", self.held_output.getvalue())
        self.assertIn("'aA' is a palindrome.", self.held_output.getvalue())
        self.assertIn("'Test' is not a palindrome.", self.held_output.getvalue())

    # Edge cases: testing empty and single-character strings
    def test_empty_string(self):
        """Test with an empty string."""
        check_palindromes([""])
        self.assertIn("'' is a palindrome.", self.held_output.getvalue())

    def test_single_character(self):
        """Test with a single character."""
        check_palindromes(["a", "1", "!"])
        self.assertIn("'a' is a palindrome.", self.held_output.getvalue())
        self.assertIn("'1' is a palindrome.", self.held_output.getvalue())
        self.assertIn("'!' is a palindrome.", self.held_output.getvalue())

    # Defensive tests: wrong input types, assertions
    def test_invalid_input_type(self):
        """Test when input is not a list."""
        with self.assertRaises(TypeError):
            check_palindromes("not a list")

    def test_non_string_elements(self):
        """Test when input list contains non-string elements."""
        with self.assertRaises(TypeError):
            check_palindromes([123, 456])


if __name__ == "__main__":
    unittest.main()
