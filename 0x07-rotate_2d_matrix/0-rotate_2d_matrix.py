#!/usr/bin/python3
"""
Rotates a two dimentional Matrix

function:
        rotate_2d_matrix(matrix)
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a two dimentional Matrix
    Args:
        matrix(list)
    Return:
        None
    """
    n = len(matrix)
    for i in range(n//2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
