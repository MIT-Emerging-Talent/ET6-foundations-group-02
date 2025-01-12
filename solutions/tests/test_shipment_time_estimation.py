#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for Shipment Time Estimation.


Test categories:
    - Standard cases: correct inputs for distance and speed
    - Edge cases
    - Defensive tests: wrong input types, assertions

Created on 2025-01-06
Author: Idris Pamiri
"""

import unittest

from ..shipment_time_estimation import shipment_time_estimation


class TestShipmentTimeEstimation(unittest.TestCase):
    """Test suite for XXXX"""

    # Standard test cases
    def test_short_distance(self):
        """It should return the time for a short distance"""
        self.assertEqual(shipment_time_estimation(10, 2), 5)

    def test_long_distance(self):
        """It should correctly calculate time for a long distance"""
        self.assertAlmostEqual(shipment_time_estimation(1500, 100), 15)

    def test_decimal_values(self):
        """It should handle decimal values correctly"""
        self.assertAlmostEqual(shipment_time_estimation(50.5, 10.1), 5.0)

    # Edge cases
    def test_zero_distance(self):
        """It should return 0 time when distance is 0"""
        self.assertEqual(shipment_time_estimation(0, 10), 0)

    def test_large_speed(self):
        """It should return a very small time when speed is large"""
        self.assertAlmostEqual(shipment_time_estimation(1, 10000), 0.0001)

    # Defensive tests (invalid input types and values)
    def test_negative_distance(self):
        """It should raise an assertion error for negative distance"""
        with self.assertRaises(AssertionError):
            shipment_time_estimation(-10, 10)

    def test_zero_speed(self):
        """It should raise an assertion error for zero speed"""
        with self.assertRaises(AssertionError):
            shipment_time_estimation(10, 0)

    def test_negative_speed(self):
        """It should raise an assertion error for negative speed"""
        with self.assertRaises(AssertionError):
            shipment_time_estimation(10, -5)

    def test_non_numeric_distance(self):
        """It should raise an assertion error for non-numeric distances"""
        with self.assertRaises(AssertionError):
            shipment_time_estimation("ten", 10)

    def test_non_numeric_speed(self):
        """It should raise an assertion error for non-numeric speed"""
        with self.assertRaises(AssertionError):
            shipment_time_estimation(10, "fast")

    def test_both_non_numeric_inputs(self):
        """It should raise an assertion error when both inputs are non-numeric"""
        with self.assertRaises(AssertionError):
            shipment_time_estimation("ten", "fast")


if __name__ == "__main__":
    unittest.main()
