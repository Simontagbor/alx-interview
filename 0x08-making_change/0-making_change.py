#!/usr/bin/python3
"""determine the fewest amount of coins needed to meet an amount"""


def makeChange(coins, total):
    """determine the fewest amount of coins needed to meet an amount"""
    if total <= 0:
        return 0
    coins.sort()
    coins.reverse()
    count = 0
    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total = total % coin
    if total != 0:
        return -1
    return count
