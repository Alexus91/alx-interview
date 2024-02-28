#!/usr/bin/python3
"""Making Change.
"""


def makeChange(coins, total):
    """Calculates the fewest number of coins needed to meet a given total.
    """
    if total <= 0:
        return 0

    # Create a list to store the fewest number of coins needed
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        if coin > total:
            continue
        count = total // coin
        total -= count * coin
        coin_count += count
        if total == 0:
            break
    if total > 0:
        return -1
    return coin_count
