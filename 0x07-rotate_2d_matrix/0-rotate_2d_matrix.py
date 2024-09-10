#!/usr/bin/python3

""" Rotate a 2D Matrix 90 Degrees Clockwise """


def rotate_2d_matrix(matrix):
    """ Rotate a 2D matrix 90 degrees clockwise in-place.
    - The matrix must be modified in-place.
    - Matrix is guaranteed to be non-empty and 2D.
    """

    n = len(matrix[0])

    for i in range(n - 1, -1, -1):
        for j in range(0, n):
            matrix[j].append(matrix[i].pop(0))
