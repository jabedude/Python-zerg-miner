#!/usr/bin/env python3
from math import hypot


class Path:

    def __init__(self):
        pass


def recursive_path(goal, grid):
    raise NotImplementedError

def linear_distance(point_one, point_two):
    return hypot(point_one[0] - point_two[0], point_one[1] - point_two[1])

def area_to_graph(area):
    graph = dict()
    print()

    for coordinate in area:
        graph[coordinate] = []
        x = coordinate[0]
        y = coordinate[1]
        north = (x, y + 1)
        south = (x, y - 1)
        east = (x + 1, y)
        west = (x - 1, y)
        if area[north] in ' *':
            graph[coordinate].append(north)
        if area[south] in ' *':
            graph[coordinate].append(south)
        if area[east] in ' *':
            graph[coordinate].append(east)
        if area[west] in ' *':
            graph[coordinate].append(west)

    print(graph)
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
