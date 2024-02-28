#!/usr/bin/python3
"""Making Change.
"""


def makeChange(coins, total):
    """Calculates the fewest number of coins needed to meet a given total.
    """
    if total <= 0:
        return 0

    # Create a list to store the fewest number of coins needed
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]
