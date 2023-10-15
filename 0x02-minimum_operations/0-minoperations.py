#!/usr/bin/python3
"""
A simple moduele for practicing dynamic programming
Function:
    minOperations(n)
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result
    in exactly n 'H' characters in the file.

    Args:
        n (int): The target number of 'H' characters to achieve.

    Returns:
        int: The minimum number of operations required
        to achieve n 'H' characters.

    If n is impossible to achieve, return 0.
    """
    if n < 1:
        return 0

    operations = 0
    d = 2

    while d * d <= n:
        while (n % d) == 0:
            n //= d
            operations += d
        d += 1

    if n > 1:
        operations += n

    return operations
