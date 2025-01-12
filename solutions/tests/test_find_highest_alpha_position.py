"""Tests for the find_highest_alpha_position function.

@author: Musab Kaymak
@created: 01/09/2025
"""

import unittest

from solutions.find_highest_alpha_position import find_highest_alpha_position


class TestFindHighestAlphaPosition(unittest.TestCase):
    """Test cases for the find_highest_alpha_position function."""

    def test_simple_word(self):
        """Test with a simple lowercase word."""
        self.assertEqual(find_highest_alpha_position("flower"), 23)

    def test_uppercase_word(self):
        """Test with an uppercase word."""
        self.assertEqual(find_highest_alpha_position("ZEBRA"), 26)

    def test_mixed_case_word(self):
        """Test with a mixed case word."""
        self.assertEqual(find_highest_alpha_position("PyThOn"), 25)

    def test_single_letter(self):
        """Test with a single letter."""
        self.assertEqual(find_highest_alpha_position("a"), 1)

    def test_with_spaces(self):
        """Test with text containing spaces."""
        self.assertEqual(find_highest_alpha_position("hello world"), 23)

    def test_with_numbers(self):
        """Test with text containing numbers."""
        self.assertEqual(find_highest_alpha_position("hello123"), 15)

    def test_with_special_characters(self):
        """Test with text containing special characters."""
        self.assertEqual(find_highest_alpha_position("hello!@#"), 15)

    def test_empty_string(self):
        """Test that empty string raises ValueError."""
        with self.assertRaises(ValueError, msg="Input text cannot be empty"):
            find_highest_alpha_position("")

    def test_no_letters(self):
        """Test that string with no letters raises ValueError."""
        with self.assertRaises(
            ValueError, msg="Input text must contain at least one letter."
        ):
            find_highest_alpha_position("123")

    def test_non_english_characters(self):
        """Test that non-English characters raise ValueError."""
        with self.assertRaises(
            ValueError, msg="Input text must contain only English characters."
        ):
            find_highest_alpha_position("héllo")
