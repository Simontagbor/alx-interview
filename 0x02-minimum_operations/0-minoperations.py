#!/usr/bin/env python3
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

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i

        for j in range(2, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]
