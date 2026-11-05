#!/usr/bin/python3
"""
Rotate 2D Matrix module.

This module provides a function to rotate an n x n 2D matrix
90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list): The 2D square matrix to rotate.

    Returns:
        None: The matrix is modified in-place.
    """
    n = len(matrix)

    # 1. Transpose the matrix (swap elements across the diagonal)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 2. Reverse each row to complete the clockwise rotation
    for i in range(n):
        matrix[i].reverse()
