#!/usr/bin/python3
"""Pascal triangle implementation."""


def pascal_triangle(n):
    """A function that returns a list of lists of integers
    representing the Pascal's triangle of n.
    Returns an empty list if n <= 0.
    """
    if (n <= 0):
        return [[]]
    else:
        if n == 1:
            return [[1]]
        else:
            result = pascal_triangle(n - 1)
            current_row = [1]
            previous_row = result[-1]
            for i in range(len(previous_row) - 1):
                current_row.append(previous_row[i] + previous_row[i + 1])
            current_row += [1]
            result.append(current_row)
            return result
