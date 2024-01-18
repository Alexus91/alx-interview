#!/usr/bin/python3
"""Minimum Operations
"""


def minOperations(n):
    """In a text file, there is a single character H. Your text editor
    can execute only two operations in this file: Copy All and Paste.
    Given a number n, this script calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
    """
    if not isinstance(n, int):
        return 0
    count = 0
    cboard = 0
    end = 1
    while end < n:
        if cboard == 0:
            cboard = end
            end += cboard
            count += 2
        elif n - end > 0 and (n - end) % end == 0:
            cboard = end
            end += cboard
            count += 2
        elif cboard > 0:
            end += cboard
            count += 1
    return count
