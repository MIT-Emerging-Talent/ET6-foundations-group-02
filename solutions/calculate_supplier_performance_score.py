#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for calculating the performance score of a supplier.
Module contents:
    - Calculates the performance score of a supplier based on delivery reliability

Created on 2025-01-07
Author: Idris Pamiri
"""

import doctest


def calculate_supplier_performance_score(
    on_time_deliveries: int,
    total_deliveries: int,
    defective_items: int,
    total_items: int,
) -> float:
    """
    Evaluates supplier performance based on delivery reliability and defect rates.

    The function calculates a performance score (0-100) by combining the percentage
    of on-time deliveries and the percentage of defect-free items. The two metrics
    are equally weighted in the score.

    Parameters:
        on_time_deliveries (int): Number of on-time deliveries.
        total_deliveries (int): Total number of deliveries (must be greater than 0).
        defective_items (int): Number of defective items.
        total_items (int): Total items delivered (must be greater than 0).

    Returns:
        float: Supplier performance score (0-100).

    Raises:
        ValueError: If any input is negative or total_deliveries/total_items is zero.

    Examples:
        >>> calculate_supplier_performance_score(45, 50, 10, 100)
        90.0
        >>> calculate_supplier_performance_score(10, 10, 0, 20)
        100.0
        >>> calculate_supplier_performance_score(0, 10, 5, 20)
        37.5
    """
    # Defensive programming with assertions
    assert isinstance(on_time_deliveries, int), "on_time_deliveries must be an integer"
    assert isinstance(total_deliveries, int), "total_deliveries must be an integer"
    assert isinstance(defective_items, int), "defective_items must be an integer"
    assert isinstance(total_items, int), "total_items must be an integer"

    if total_deliveries <= 0:
        raise ValueError("Total deliveries must be greater than zero")
    if total_items <= 0:
        raise ValueError("Total items must be greater than zero")
    if on_time_deliveries < 0 or defective_items < 0:
        raise ValueError("on_time_deliveries and defective_items cannot be negative")
    if on_time_deliveries > total_deliveries:
        raise ValueError("on_time_deliveries cannot exceed total_deliveries")
    if defective_items > total_items:
        raise ValueError("defective_items cannot exceed total_items")

    # Calculate delivery score and defect score
    delivery_score = (on_time_deliveries / total_deliveries) * 100
    defect_score = ((total_items - defective_items) / total_items) * 100

    # Calculate overall performance score
    performance_score = (delivery_score + defect_score) / 2

    return performance_score


if __name__ == "__main__":
    doctest.testmod()
