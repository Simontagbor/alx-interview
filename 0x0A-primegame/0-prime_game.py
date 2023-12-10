#!/usr/bin/python3
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

    maria_prime_list = []
    ben_prime_list = []

    for index in range(x):
        number_pool = [i for i in range(1, nums[index] + 1)]
        prime_pool = [num for num in number_pool if is_prime(num)]
        last_player = None

        while prime_pool:
            # Maria's turn
            if prime_pool:
                maria_prime = min(prime_pool)
                prime_pool = [num for num in prime_pool
                              if num % maria_prime != 0]
                last_player = "Maria"

            # Ben's turn
            if prime_pool:
                ben_prime = min(prime_pool)
                prime_pool = [num for num in prime_pool
                              if num % ben_prime != 0]
                last_player = "Ben"

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
