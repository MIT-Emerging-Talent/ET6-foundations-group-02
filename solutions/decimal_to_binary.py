# solutions/convert_decimal_to_binary.py

"""
This module provides a function to convert a non-negative integer to its binary representation.

Function:
    - convert_decimal_to_binary: Returns the binary representation of a given non-negative integer.
Author: Melat Assefa
Date: January 6, 2025 
"""


def convert_decimal_to_binary(n: int) -> str:
    """
    Converts a non-negative integer to its binary representation.

    Parameters:
        n (int): A non-negative integer to be converted to binary.

    Returns:
        str: The binary representation of the given integer.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> convert_decimal_to_binary(0)
        '0'
        >>> convert_decimal_to_binary(5)
        '101'
        >>> convert_decimal_to_binary(23)
        '10111'
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    return bin(n)[2:]
