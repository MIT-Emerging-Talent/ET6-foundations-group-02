"""Module for finding the highest alphabetical position in a text string.

This module provides functionality to find the alphabetical position (1-26)
of the character that appears latest in the alphabet within a given text.

@author: Musab Kaymak
@created: 01/09/2025
"""


def find_highest_alpha_position(text: str) -> int:
    """Find the alphabetical position of the latest alphabet character in text.

    Parameters:
        text (str): The input text to analyze. Must contain at least one letter
            and only contain English letters. Numbers and special characters are ignored.

    Returns:
        int: The highest alphabetical position (1-26) found in the text.
            'a' is position 1, 'z' is position 26.

    Raises:
        ValueError: If the text is empty or contains no letters.
        ValueError: If the text contains non-ASCII letters.

    Examples:
        >>> find_highest_alpha_position("flower")
        23
        >>> find_highest_alpha_position("apple")
        16
        >>> find_highest_alpha_position("ZEBRA")
        26
    """
    if not text:
        raise ValueError("Input text cannot be empty")

    if not any(c.isalpha() for c in text):
        raise ValueError("Input text must contain at least one letter")

    if not all(c.isascii() for c in text):
        raise ValueError("Input text must contain only English characters")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    max_position = 0

    for char in text.lower():
        if char.isalpha():
            position = alphabet.index(char.lower()) + 1
            if position > max_position:
                max_position = position

    return max_position
