#!/usr/bin/python3

""" Minimum Operations """


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly
    n 'H' characters in a file using only copy and paste operations.

    Returns an integer.
    If n is impossible to achieve, returns 0.
    """
    if not isinstance(n, int):
        return 0

    operations = 0
    iterator = 2
    while iterator <= n:
        if n % iterator == 0:
            n //= iterator
            operations += iterator
            iterator = 1
        iterator += 1
    return operations
