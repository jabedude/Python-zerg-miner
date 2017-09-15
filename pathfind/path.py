#!/usr/bin/env python3
from math import hypot


class Path:

    def __init__(self):
        pass


def recursive_path(goal, grid):
    raise NotImplementedError

def linear_distance(point_one, point_two):
    return hypot(point_one[0] - point_two[0], point_one[1] - point_two[1])
