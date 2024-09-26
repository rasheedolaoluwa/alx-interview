#!/usr/bin/python3

""" Function to calculate the perimeter of an island represented in a grid """


def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the grid.
    Args:
        grid: A list of lists representing the island.
    Returns:
        The perimeter of the island.
    """
    count = 0
    row = len(grid)
    col = len(grid[0]) if row else 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):

            # Check the four neighboring positions (up, left, right, down)
            idx = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
            check = [1 if k[0] in range(row) and k[1] in range(col) else 0
                     for k in idx]

            # If current cell is land (1), count the number of
            # water (0) edges around it
            if grid[i][j]:
                count += sum([1 if not r or not grid[k[0]][k[1]] else 0
                              for r, k in zip(check, idx)])

    return count
