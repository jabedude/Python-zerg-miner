#!/usr/bin/env python3
'''Module implements several helper functions used during pathfinding'''

from math import hypot


def linear_distance(point_one, point_two):
    '''Calucates the distance between two coordinates'''
    return hypot(point_one[0] - point_two[0], point_one[1] - point_two[1])


def area_to_graph(area, goal=None):
    '''Converts a zerg map to a graph using an adjacency list'''
    graph = dict()
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
    '''
    Gnerate paths witha breadth-first-search.
    http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
    '''
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    '''Return the shortest path from a generator of paths'''
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


def generate_cardinality(coordinates):
    '''Convert a set of coordinate instructions to compass directions'''
    if not coordinates:
        return ['CENTER']
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
