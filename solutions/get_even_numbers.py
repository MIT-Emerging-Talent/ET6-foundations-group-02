#!/usr/bin/env/python3
"""
This module contains a function to get even numbers from a list of integers.

Function:
    - get_even_numbers: Takes a list of integers and returns a list of even integers.
Created on: January 6, 2025
@author: Melat Assefa
"""

from typing import List


def get_even_numbers(numbers: List[int]) -> List[int]:
    """
    Filters and returns all even numbers from the input list of integers.

    Parameters:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list containing only the even integers from the input list.

    Behavior:
        - The function iterates through the input list and checks each integer.
        - If the integer is divisible by 2, it's included in the result.

    Examples:
        >>> get_even_numbers([1, 2, 3, 4, 5])
        [2, 4]
        >>> get_even_numbers([10, 15, 20, 25])
        [10, 20]
        >>> get_even_numbers([])
        []

    Assumptions:
        - The input is always a list of integers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    return [num for num in numbers if num % 2 == 0]
