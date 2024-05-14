#!/usr/bin/python3
"""Prime Game problem."""


def primes(n):
    """
    Prime number determiner function.
    Args:
        - n (int): upper boundary of range. lower boundary is always 1
    Returns: list of prime numbers between 1 and n inclusive
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Determine the winner of each game played by Maria and Ben.

    Args:
    - x (int): The number of rounds played.
    - nums (list of int): An array containing the value of n for each round.

    Returns:
    - str or None: The name of the player who won the most rounds.
    If the winner cannot be determined, returns None.

    Constraints:
    - Both x and n will not be larger than 10000.
    - No packages are imported.

    Example:
    isWinner(3, [4, 5, 1]) returns "Ben"
    First round: 4
    Maria picks 2 and removes 2, 4, leaving 1, 3
    Ben picks 3 and removes 3, leaving 1
    Ben wins because there are no prime numbers left for Maria to choose

    Second round: 5
    Maria picks 2 and removes 2, 4, leaving 1, 3, 5
    Ben picks 3 and removes 3, leaving 1, 5
    Maria picks 5 and removes 5, leaving 1
    Maria wins because there are no prime numbers left for Ben to choose

    Third round: 1
    Ben wins because there are no prime numbers for Maria to choose

    Result: Ben has the most wins
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    return None
