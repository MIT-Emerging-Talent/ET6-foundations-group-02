#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module estimation of delivery time based on 2 argument

Module contents:
    - Calculates the estimated delivery time based on the distance and average speed.

Created on 2025-01-06
Author: Idris Pamiri
"""


def shipment_time_estimation(distance: float, average_speed: float) -> float:
    """
    Estimate the delivery time based on distance and average speed.

        Parameters:
        distance (float): The distance to the delivery location in kilometers.
        average_speed (float): The average speed of the delivery trucks in kilometers per hour.

        Returns:
        float: The estimated delivery time in hours.

        Preconditions:
        - distance must be a non-negative float or int.
        - average_speed must be a positive float or int.

        Raises:
        AssertionError: If any of the preconditions are violated.

        Examples:
        >>> shipment_time_estimation(100, 50)
        2.0
        >>> shipment_time_estimation(1500, 100)
        15.0
        >>> shipment_time_estimation(0, 10)
        0.0


        AssertionError: average_speed must be greater than zero.
        AssertionError: distance must be non-negative.
    """

    # Defensive checks with assertions
    assert isinstance(distance, (int, float)), (
        "distance must be a number (int or float)."
    )
    assert distance >= 0, "distance must be non-negative."
    assert isinstance(average_speed, (int, float)), (
        "average_speed must be a number (int or float)."
    )
    assert average_speed > 0, "average_speed must be greater than zero."

    # Assign received arguments to local variables - for debugging purpose only
    local_distance = distance

    local_average_speed = average_speed

    # Calculate the shipment time using local variables
    estimated_time = local_distance / local_average_speed

    return estimated_time
