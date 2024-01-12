#!/usr/bin/python3
""" Prime Game
Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including n, they take turns choosing a prime
number from the set and removing that number and its multiples from the
set. The player that cannot make a move loses the game.
They play x rounds of the game, where n may be different for each round.
"""


def is_prime(n):
    """ Checks if a number is prime
    Args:
        n: number to check
    Returns:
        True if n is prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """ Prime Game
    Args:
        x: number of rounds
        nums: array of n
        Returns:
            name of the player that won the most rounds
            If the winner cannot be determined, return None
    """
    maria_wins = 0
    ben_wins = 0
    for num in nums:
        prime_pool = [i for i in range(2, num + 1) if all(i % j != 0 for j in range(2, i))]
        last_player = ""
        ben_prime = None
        while prime_pool:
            if last_player == "Maria":
                ben_prime = max(prime_pool)
                last_player = "Ben"
            else:
                maria_prime = min(prime_pool)
                last_player = "Maria"
            if ben_prime is not None:
                prime_pool = [num for num in prime_pool if num % ben_prime != 0]
        if last_player == "Maria":
            maria_wins += 1
        elif last_player == "Ben":
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
