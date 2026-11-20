#!/usr/bin/python3
"""
This module defines a function to calculate the perimeter of an island.
"""


def island_perimeter(grid):
    """
    Calculate the total perimeter of the island represented in the grid.

    Args:
        grid (list of list of int): A 2D grid where 0 is water and 1 is land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 sides for each land cell found
                perimeter += 4

                # Subtract 2 shared sides if the upper cell is also land
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # Subtract 2 shared sides if the left cell is also land
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
