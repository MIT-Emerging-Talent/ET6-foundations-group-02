"""
Module resolving FizzBuzz problem according to given rules.

Module contents:
    - fizzbuzz: take integer n and prints numbers from 1 to n
        with the rules.

Created: 01/04/2025
Author: Svitlana Musiienko

"""


def fizzbuzz(n: int) -> list:
    """
    Fizzbuz function takes an integer n as input and prints the numbers
    from 1 to n with the rules:
        - if a number is divisible by 3, print 'Fizz' instead of the number;
        - if a number is divisible by 5, print 'Buzz' instead of the number;
        - if a number is divisible by both 3 and 5, print 'FizzBuzz';
        - otherwise, print the number itself.

    Parameters: integer number (n)

    Returns: return list of numbers from 1 to n where numbers
    divisible by 3 and 5 are replaced with fizz and buzz and fizzbuzz

    Raises:
        AssertionError: if the argument is not integer
        AssertionError: if the argument is less than 0

    Example:

    >>> fizzbuzz (0)
    []

    >>> fizzbuzz (5)
    [1, 2, 'Fizz', 4, 'Buzz']

    >>> fizzbuzz(15)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']

    """
    # the number should be an integer greater than 0
    assert isinstance(n, int)
    # the number is less than 0
    assert n >= 0

    result = []
    # loop through numbers from 1 to n
    for num in range(1, n + 1):
        # check if the number is divisible by both 3 and 5
        if num % 3 == 0 and num % 5 == 0:
            # print "FizzBuzz" for multiples of both 3 and 5
            result.append("FizzBuzz")
        # check if the number is divisible by 3 only
        elif num % 3 == 0:
            # print "Fizz" for multiples of 3
            result.append("Fizz")
        # check if the number is divisible by 5 only
        elif num % 5 == 0:
            # print "Buzz" for multiples of 5
            result.append("Buzz")
        # print the number if none of the above conditions are met
        else:
            result.append(num)
    return result
