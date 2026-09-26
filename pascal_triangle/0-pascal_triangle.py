#!/usr/bin/python3
"""
This module provides a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle integers up to n rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of list of int: A matrix representing the triangle layout,
                             or an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []
    while len(triangle) < n:
        if not triangle:
            triangle.append([1])
        else:
            last_row = triangle[-1]
            new_row = [1]
            for i in range(len(last_row) - 1):
                new_row.append(last_row[i] + last_row[i + 1])
            new_row.append(1)
            triangle.append(new_row)

    return triangle
