"""
Module for checking if given words or numbers are palindromes.

This module checks a list of strings and numbers to determine if each one
is a palindrome (reads the same forward and backward). The check is done
for multiple inputs using a for loop.

Author: fevziismailsahin
Created: 01/10/2025
"""

from typing import List


def check_palindromes(words_to_check: List[str]) -> None:
    """
    Function check_palindromes checks if each word or number in the list is a palindrome.

    Parameters:
    words_to_check (List[str]): A list of strings and numbers to check for palindrome

    Returns:
    None:
        Prints whether each word or number in the list is a palindrome or not

    Example:

    >>> check_palindromes(["Radar", "12321", "Hello", "1.232.1", "12345", "aA", "Test"])
    'Radar' is a palindrome.
    '12321' is a palindrome.
    'Hello' is not a palindrome.
    '1.232.1' is a palindrome.
    '12345' is not a palindrome.
    'aA' is a palindrome.
    'Test' is not a palindrome.

    """
    if not isinstance(words_to_check, list):
        raise TypeError("Input must be a list")

    for value in words_to_check:
        if not isinstance(value, str):
            raise TypeError("List must contain only strings")
        cleaned_value = "".join(filter(str.isalnum, value)).lower()

        if cleaned_value == cleaned_value[::-1]:
            print(f"'{value}' is a palindrome.")
        else:
            print(f"'{value}' is not a palindrome.")
