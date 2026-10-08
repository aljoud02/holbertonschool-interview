#!/usr/bin/python3
"""Module for calculating the minimum operations to reach n characters."""


def minOperations(n):
    """Calculates the fewest number of operations needed to result in n H."""
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
