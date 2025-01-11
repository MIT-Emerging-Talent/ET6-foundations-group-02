"""
Module for generating and displaying ASCII art of a pine tree.

This module provides a function to create a visual representation of a pine tree
with customizable height and trunk dimensions.

Author: fevziismailsahin
Created: 01/09/2025
"""


def draw_tree(height: int = 10, trunk_width: int = 3, trunk_height: int = 3) -> str:
    """
    Generate an ASCII art representation of a pine tree.

    Parameters:
        height (int): The height of the tree (default is 10).
        trunk_width (int): The width of the tree trunk (default is 3).
        trunk_height (int): The height of the tree trunk (default is 3).

    Returns:
        str: The generated ASCII art as a string.

    Example:
        >>> print(draw_tree(height=5, trunk_width=3, trunk_height=2))
             *
            ***
           *****
          *******
         *********
            |||
            |||
    """
    # Defensive assertions
    if height <= 0:
        raise ValueError("Height must be a positive integer")
    if trunk_width <= 0:
        raise ValueError("Trunk width must be a positive integer")
    if trunk_height <= 0:
        raise ValueError("Trunk height must be a positive integer")

    # Create the foliage of the tree
    tree = []
    for i in range(height):
        spaces = " " * (height - i - 1)  # Add spaces for alignment (center the stars)
        stars = "*" * (2 * i + 1)  # Create the stars for the current level
        tree.append(spaces + stars)  # Append to tree list with correct alignment

    # Create the trunk of the tree
    trunk = " " * (height - trunk_width // 2 - 1) + "|" * trunk_width  # Centered trunk
    for _ in range(trunk_height):
        tree.append(trunk)

    # Return the tree as a single string
    return "\n".join(tree)


if __name__ == "__main__":
    print(draw_tree())
