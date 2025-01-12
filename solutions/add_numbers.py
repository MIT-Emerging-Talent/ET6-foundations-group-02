# add_numbers.py

"""
This module provides a function to add two numbers.

Function:
    - add_numbers: float: The sum of the two numbers.
Created on: January 6, 2025
@author: Melat Assefa
"""


def add_numbers(a: float, b: float) -> float:
    """
    Calculate the sum of two numbers.

    Parameters:
    a (float): The first number to add. It can be any real number.
    b (float): The second number to add. It can be any real number.

    Returns:
    float: The sum of the two numbers.

    Raises:
    TypeError: If either of the arguments is not a number.

    Examples:
    >>> add_numbers(2, 3)
    5
    >>> add_numbers(-1, 1)
    0
    >>> add_numbers(0.5, 0.5)
    1.0
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers.")

    return a + b
