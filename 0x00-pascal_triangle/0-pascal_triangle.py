#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for _ in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, len(prev_row)):
            new_number = prev_row[j - 1] + prev_row[j]
            new_row.append(new_number)

        new_row.append(1)
        triangle.append(new_row)

    return triangle
