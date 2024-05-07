#!/usr/bin/python3
"""Module defining island perimeter finding function."""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
    - grid (list): A list of lists of integers representing the grid where:
        - 0 represents water
        - 1 represents land
        - Each cell is square, with a side length of 1
        - Cells are connected horizontally/vertically (not diagonally)
        - grid is rectangular, with its width and height not exceeding 100
        - The grid is completely surrounded by water
        - There is only one island (or nothing)
        - The island doesn't have “lakes” (water inside that isn't connected
        to the water surrounding the island)

    Returns:
    - int: The perimeter of the island.
    """
    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                if j > 0 and grid[i][j - 1] == 1:
                    edges += 1
                if i > 0 and grid[i - 1][j] == 1:
                    edges += 1
    return size * 4 - edges * 2
