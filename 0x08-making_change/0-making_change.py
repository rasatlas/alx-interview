#!/usr/bin/python3
"""Module solving the classic coin change problem."""


def makeChange(coins, total):
    """Calculates the minimum number of coins needed to make a specific amount.
    Args:
        coins ([int]): A list of coin denominations (positive int).
        total (int): The total amount to make change for (non-negative int).
    Returns:
        The minimum number of coins needed to make the total amount,
        or 0 if total is 0,
        or -1 if it's impossible to make the total amount with the given coins.
    Raises:
        ValueError: If the coin list contains a non-positive value.
    """
    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    try:
        # check if the target total amount can be directly formed using
        # one of the coin denominations available in the list coins.

        target = coins.index(total)

        # If total can be formed using a single coin denomination,
        # then 'target' will be assigned the index of that coin denomination
        # in the list coins. Since it's possible to form the total amount with
        # a single coin, the function returns 1 immediately.

        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    coin_count = 0
    for i in coins:
        if total % i == 0:
            coin_count += int(total / i)
            return coin_count
        if total - i >= 0:
            if int(total / i) > 1:
                coin_count += int(total / i)
                total = total % i
            else:
                coin_count += 1
                total -= i
                if total == 0:
                    break
    if total > 0:
        return -1
    return coin_count
