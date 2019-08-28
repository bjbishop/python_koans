#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#


def triangle(a, b, c):
    if a == 0 or b == 0 or c == 0:
        raise TriangleError('0 length side')

    if a < 0 or b < 0 or c < 0:
        raise TriangleError('negative length side')

    sorted_lengths = sorted(list([a, b, c]))
    equal_sides = len(set({a, b, c}))

    if equal_sides == 3:
        return 'scalene'
    elif equal_sides == 2:
        if sorted_lengths[0] + sorted_lengths[1] < sorted_lengths[2]:
            raise TriangleError('sum of two sides not greater than 3rd side')
        else:
            return 'isosceles'
    else:
        return 'equilateral'


# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
