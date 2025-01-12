#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for Calculating the performance score of a supplier.

Test categories:
    - Standard cases: correct inputs for on_time_deliveries, total_deliveries,
    defective_items, total_items;
    - Edge cases;
    - Defensive tests: wrong input types, assertions;

Created on 2025-01-07
Author: Idris Pamiri
"""

import unittest

from ..calculate_supplier_performance_score import calculate_supplier_performance_score


class TestCalculatingPerformanceScore(unittest.TestCase):
    """Test suite for Calculating the performance score of a supplier."""

    # Standard cases: correct inputs
    def test_standard_case_1(self):
        """Test with typical valid inputs for on-time deliveries, total deliveries,
        defective items, and total items."""
        self.assertAlmostEqual(
            calculate_supplier_performance_score(45, 50, 10, 100), 90.0
        )

    def test_standard_case_2(self):
        """Test with perfect performance: 100% on-time deliveries and defect-free items."""
        self.assertAlmostEqual(
            calculate_supplier_performance_score(10, 10, 0, 20), 100.0
        )

    def test_standard_case_3(self):
        """Test with partial performance: some defective items and partial on-time deliveries."""
        self.assertAlmostEqual(calculate_supplier_performance_score(0, 10, 5, 20), 37.5)

    # Edge cases: testing zero or near-zero values
    def test_zero_deliveries(self):
        """Test when total deliveries is zero, which should raise a ValueError."""
        with self.assertRaises(ValueError):
            calculate_supplier_performance_score(0, 0, 0, 10)

    def test_zero_items(self):
        """Test when total items is zero, which should raise a ValueError."""
        with self.assertRaises(ValueError):
            calculate_supplier_performance_score(5, 10, 1, 0)

    def test_full_performance(self):
        """Test when all deliveries are on time and there are no defective item(s),
        which should return a 100% score."""
        self.assertAlmostEqual(
            calculate_supplier_performance_score(100, 100, 0, 100), 100.0
        )

    def test_zero_performance(self):
        """Test when all deliveries are late and defective, which should return a 0% score."""
        self.assertAlmostEqual(calculate_supplier_performance_score(0, 10, 10, 10), 0.0)

    # Defensive tests: wrong input types, assertions
    def test_invalid_on_time_deliveries_type(self):
        """Test when 'on_time_deliveries' is not an integer, which should
        raise an AssertionError."""
        with self.assertRaises(AssertionError):
            calculate_supplier_performance_score("five", 10, 2, 100)

    def test_invalid_total_deliveries_type(self):
        """Test when 'total_deliveries' is not an integer, which should raise an AssertionError."""
        with self.assertRaises(AssertionError):
            calculate_supplier_performance_score(10, "ten", 2, 100)

    def test_invalid_defective_items_type(self):
        """Test when 'defective_items' is not an integer, which should raise an AssertionError."""
        with self.assertRaises(AssertionError):
            calculate_supplier_performance_score(10, 10, "two", 100)

    def test_invalid_total_items_type(self):
        """Test when 'total_items' is not an integer, which should raise an AssertionError."""
        with self.assertRaises(AssertionError):
            calculate_supplier_performance_score(10, 10, 2, "hundred")

    def test_negative_on_time_deliveries(self):
        """Test when 'on_time_deliveries' is negative, which should raise a ValueError."""
        with self.assertRaises(ValueError):
            calculate_supplier_performance_score(-5, 10, 2, 100)

    def test_negative_defective_items(self):
        """Test when 'defective_items' is negative, which should raise a ValueError."""
        with self.assertRaises(ValueError):
            calculate_supplier_performance_score(10, 10, -2, 100)

    def test_on_time_deliveries_exceed_total_deliveries(self):
        """Test when 'on_time_deliveries' exceeds 'total_deliveries', which should
        raise a ValueError."""
        with self.assertRaises(ValueError):
            calculate_supplier_performance_score(15, 10, 2, 100)

    def test_defective_items_exceed_total_items(self):
        """Test when 'defective_items' exceeds 'total_items', which
        should raise a ValueError."""
        with self.assertRaises(ValueError):
            calculate_supplier_performance_score(10, 10, 120, 100)


if __name__ == "__main__":
    unittest.main()
