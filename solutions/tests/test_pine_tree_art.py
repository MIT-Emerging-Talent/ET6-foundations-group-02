#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit test module for generating ASCII art of a pine tree.

Test categories:
    - Standard cases: correct inputs for height, trunk_width, trunk_height;
    - Edge cases;
    - Defensive tests: wrong input types, assertions;

Created on 2025-01-11
Author: fevziismailsahin
"""

import unittest

from ..pine_tree_art import pine_tree_art


class TestPineTreeArt(unittest.TestCase):
    """Test suite for generating ASCII art of a pine tree."""

    # Standard cases: correct inputs
    def test_standard_case_1(self):
        """Test with typical valid inputs for height, trunk_width, trunk_height."""
        expected_result = (
            "         *\n"
            "        ***\n"
            "       *****\n"
            "      *******\n"
            "     *********\n"
            "    ***********\n"
            "   *************\n"
            "  ***************\n"
            " *****************\n"
            "*******************\n"
            "        |||\n"
            "        |||\n"
            "        |||\n"
        )
        self.assertEqual(pine_tree_art(10, 3, 3), expected_result)

    def test_standard_case_2(self):
        """Test with smaller tree height and trunk dimensions."""
        expected_result = (
            "    *\n   ***\n  *****\n *******\n*********\n   |||\n   |||\n   |||\n"
        )
        self.assertEqual(pine_tree_art(5, 3, 3), expected_result)

    # Edge cases: testing zero or near-zero values
    def test_zero_height(self):
        """Test when height is zero, which should raise a ValueError."""
        with self.assertRaises(ValueError):
            pine_tree_art(0, 3, 3)

    def test_zero_trunk_width(self):
        """Test when trunk width is zero, which should raise a ValueError."""
        with self.assertRaises(ValueError):
            pine_tree_art(10, 0, 3)

    def test_zero_trunk_height(self):
        """Test when trunk height is zero, which should raise a ValueError."""
        with self.assertRaises(ValueError):
            pine_tree_art(10, 3, 0)

    # Defensive tests: wrong input types, assertions
    def test_invalid_height_type(self):
        """Test when 'height' is not an integer, which should raise a TypeError."""
        with self.assertRaises(TypeError):
            pine_tree_art("ten", 3, 3)

    def test_invalid_trunk_width_type(self):
        """Test when 'trunk_width' is not an integer, which should raise a TypeError."""
        with self.assertRaises(TypeError):
            pine_tree_art(10, "three", 3)

    def test_invalid_trunk_height_type(self):
        """Test when 'trunk_height' is not an integer, which should raise a TypeError."""
        with self.assertRaises(TypeError):
            pine_tree_art(10, 3, "three")


if __name__ == "__main__":
    unittest.main()
