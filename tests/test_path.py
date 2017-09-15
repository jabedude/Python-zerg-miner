#!/usr/bin/env python3

import unittest
import sys
sys.path.append("..")
from pathfind import path
from area import Area


class TestPath(unittest.TestCase):

    def test_linear_distance(self):
        one = (-2, 1)
        two = (1, 5)
        distance = path.linear_distance(one, two)
        self.assertEqual(distance, 5)

    def test_area_to_graph(self):
        a = Area()
        test_map = {
            (0, 0): '_',
            (0, 1): ' ',
            (1, 0): '#',
            (1, -1): '#',
            (0, -1): '#',
            (-1, 0): ' ',
            (-1, -2): ' ',
            (-1, 1): ' ',
            (1, 1): ' ',
            (0, 2): '*'
        }
        a._data = test_map
        g = path.area_to_graph(a)
        p = path.bfs_paths(g, (0, 0), (0, 2))
        print(list(p))
