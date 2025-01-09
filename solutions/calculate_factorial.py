# factorial.py

"""
This module provides a function to calculate the factorial of a non-negative integer.

Function:
    - calculate_factorial: Returns the factorial of a given non-negative integer.
Author: Melat Assefa
Date: January 6, 2025    
"""


def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer.

    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the given integer.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> calculate_factorial(5)
        120
        >>> calculate_factorial(0)
        1
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
