#!/usr/bin/python3

""" Prime Game Algorithm Python """


def is_prime(n):
    """
    Checks if a number n is prime
    Iterates from 2 to the square root of n to check divisibility
    If n is divisible by any number, it is not prime
    """
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:  # If n is divisible by i, it's not prime
            return False
    return True  # If no divisors are found, n is prime


def calculate_primes(n, primes):
    """
    Calculate all primes up to a given number n
    If n is greater than the largest calculated prime, append new primes
    """
    top_prime = primes[-1]  # Get the last prime calculated
    if n > top_prime:
        for i in range(top_prime + 1, n + 1):
            if is_prime(i):
                primes.append(i)  # Append prime numbers
            else:
                primes.append(0)  # Append 0 for non-prime numbers


def isWinner(x, nums):
    """
    Determine the winner after x rounds of the game.

    x: Number of rounds
    nums: Array of integers representing the maximum number for each round

    Return: Name of the player who won the most rounds or
    None if there is no clear winner
    """

    players_wins = {"Maria": 0, "Ben": 0}  # Dictionary to keep track of wins

    primes = [0, 0, 2]

    calculate_primes(max(nums), primes)

    for round in range(x):
        # Count how many prime numbers are <= the number for this round
        sum_options = sum((i != 0 and i <= nums[round])
                          for i in primes[:nums[round] + 1])

        if (sum_options % 2):  # If the number of primes is odd, Maria wins
            winner = "Maria"
        else:  # If even, Ben wins
            winner = "Ben"

        if winner:
            players_wins[winner] += 1  # Increment the winner's count

    # Determine who won the most rounds
    if players_wins["Maria"] > players_wins["Ben"]:
        return "Maria"
    elif players_wins["Ben"] > players_wins["Maria"]:
        return "Ben"

    return None  # Return None if neither player won more rounds
