#!/usr/bin/env python3
from math import hypot
import copy


class Path:

    def __init__(self):
        pass


def recursive_path(goal, grid):
    raise NotImplementedError

def linear_distance(point_one, point_two):
    return hypot(point_one[0] - point_two[0], point_one[1] - point_two[1])

def area_to_graph(area, goal=None):
    graph = dict()
    area = copy.deepcopy(area)
    if goal is not None:
        area[goal] = ' '

    for coordinate in area:
        graph[coordinate] = []
        x = coordinate[0]
        y = coordinate[1]
        north = (x, y + 1)
        south = (x, y - 1)
        east = (x + 1, y)
        west = (x - 1, y)
        if area[north] in ' _':
            graph[coordinate].append(north)
        if area[south] in ' _':
            graph[coordinate].append(south)
        if area[east] in ' _':
            graph[coordinate].append(east)
        if area[west] in ' _':
            graph[coordinate].append(west)
    return graph

def bfs_paths(graph, start, goal):
    '''http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/'''
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

def generate_cardinality(coordinates):
    directions = list()
    for coord, prev in zip(coordinates[1:], coordinates):
        if (prev[0], prev[1] + 1) == coord:
            directions.append('NORTH')
        elif (prev[0], prev[1] - 1) == coord:
            directions.append('SOUTH')
        elif (prev[0] + 1, prev[1]) == coord:
            directions.append('EAST')
        elif (prev[0] - 1, prev[1]) == coord:
            directions.append('WEST')
    return directions
