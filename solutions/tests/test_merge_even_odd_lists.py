"""Test module for merge_even_odd_lists function.

@author: MUSABKAYMAK
@created: 01/05/2025
"""

import unittest

from solutions.merge_even_odd_lists import merge_even_odd_lists


class TestMergeEvenOddLists(unittest.TestCase):
    """Test cases for merge_even_odd_lists function."""

    def test_typical_case(self):
        """Test for lists containing typical mixed numbers."""
        result = merge_even_odd_lists([4, 12, 7, 26, 34], [6, 13, 25, 18, 47])
        assert result == [4, 12, 26, 34, 13, 25, 47]

    def test_no_even_numbers_in_first_list(self):
        """Test when first list has no even numbers."""
        result = merge_even_odd_lists([1, 3, 5], [2, 4, 7, 9])
        assert result == [7, 9]

    def test_no_odd_numbers_in_second_list(self):
        """Test when second list has no odd numbers."""
        result = merge_even_odd_lists([1, 2, 4], [2, 4, 6])
        assert result == [2, 4]

    def test_non_list_first_parameter(self):
        """Test when first parameter is not a list."""
        with self.assertRaises(TypeError, msg="Both arguments must be lists"):
            merge_even_odd_lists("not a list", [1, 2, 3])

    def test_non_list_second_parameter(self):
        """Test when second parameter is not a list."""
        with self.assertRaises(TypeError, msg="Both arguments must be lists"):
            merge_even_odd_lists([1, 2, 3], "not a list")

    def test_non_integer(self):
        """Test with non-integer items."""
        with self.assertRaises(TypeError, msg="All elements must be integers"):
            merge_even_odd_lists([1, "2", 3], [4, 5, 6])

    def test_single_number_lists(self):
        """Test with single number lists."""
        result = merge_even_odd_lists([2], [3])
        assert result == [2, 3]

    def test_negative_numbers(self):
        """Test with negative numbers."""
        result = merge_even_odd_lists([-2, -4, -1], [-6, -3, -5])
        assert result == [-2, -4, -3, -5]
