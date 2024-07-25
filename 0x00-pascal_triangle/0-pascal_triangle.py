#!/usr/bin/python3
'''
    Pascal's Triangle Function.
'''


def pascal_triangle(n):
    '''
        Function to create Pascal's Triangle.
    '''
    if n <= 0:
        return ([])
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    triangle = [[1], [1, 1]]
    for x in range(2, n):
        row = [1]
        for y in range(1, x):
            row.append(triangle[x-1][y-1] + triangle[x-1][y])
        row.append(1)
        triangle.append(row)
    return triangle
