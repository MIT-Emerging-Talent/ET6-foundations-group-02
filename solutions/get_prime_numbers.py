# prime_numbers.py

"""
This module provides a function to find all prime numbers up to a given integer.

Function:
    - get_prime_numbers: Returns a list of prime numbers less than or equal to a given integer.
Created on: January 6, 2025
@author: Melat Assefa
"""

from typing import List


def get_prime_numbers(n: int) -> List[int]:
    """
    Returns a list of all prime numbers less than or equal to the given integer.

    Parameters:
        n (int): The upper limit integer to find prime numbers up to.

    Returns:
        List[int]: A list of prime numbers less than or equal to n.

    Raises:
        ValueError: If n is less than 2.
        TypeError: If n is not an integer.

    Examples:
        >>> get_prime_numbers(10)
        [2, 3, 5, 7]
        >>> get_prime_numbers(2)
        [2]
        >>> get_prime_numbers(1)
        []
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 2:
        return []

    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
