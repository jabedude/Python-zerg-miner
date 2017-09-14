#!/usr/bin/env python3

import unittest
import sys
sys.path.append("..")
from area import Area


class TestScout(unittest.TestCase):

    def test_area_creation(self):
        a = Area()
        self.assertIsInstance(a, Area)

    def test_area_set_coordinate(self):
        a = Area()
        coordinates = (1, 0)
        tile = " "
        a[coordinates] = tile
        self.assertEqual(a[coordinates], tile)

    def test_area_set_multiple_coordinate(self):
        a = Area()
        coord = (1, 0)
        tile = "*"
        a[coord] = tile
        coord2 = (1, 1)
        a[coord2] = tile
        self.assertEqual(a[coord], tile)
        self.assertEqual(a[coord2], tile)

    def test_area_string_full_graph(self):
        a = Area()
        expected = '''  ~ * 
  _ # 
~ * # 
'''
        test_map = {
            (0, 0): '_',
            (1, 0): '#',
            (1, 1): '#',
            (0, 1): '*',
            (-1, 1): '~',
            (-1, 0): ' ',
            (-1, -1): ' ',
            (0, -1): '~',
            (1, -1): '*',
        }
        a._data = test_map
        self.assertEqual(a.__str__(), expected)

    def test_area_string_unexplored_graph(self):
        a = Area()
        expected = '''? ? * 
  ? # 
? * # 
'''
        test_map = {
            (1, 0): '#',
            (1, 1): '#',
            (0, 1): '*',
            (-1, 0): ' ',
            (1, -1): '*',
        }
        a._data = test_map
        self.assertEqual(a.__str__(), expected)

    def test_area_contains_minerals(self):
        a = Area()
        test_map = {
            (0, 0): '_',
            (0, 1): '*',
            (-1, 0): ' ',
            (-1, -1): ' ',
            (-4, -1): ' ',
            (-5, -1): ' ',
            (-6, -1): ' ',
            (-1, 7): ' ',
        }
        a._data = test_map
        self.assertIn('*', a)

    def test_area_does_not_contain_acid(self):
        a = Area()
        test_map = {
            (0, 0): '_',
            (0, 1): '*',
            (-1, 0): ' ',
            (-1, -1): ' ',
            (-4, -1): ' ',
            (-5, -1): ' ',
            (-6, -1): ' ',
            (-1, 7): ' ',
        }
        a._data = test_map
        self.assertNotIn('~', a)

    def test_area_contains_coordinate(self):
        a = Area()
        test_map = {
            (0, 0): '_',
            (0, 1): '*',
            (-1, 0): ' ',
            (-1, -1): ' ',
            (-4, -1): ' ',
            (-5, -1): ' ',
            (-6, -1): ' ',
            (-1, 7): ' ',
        }
        a._data = test_map
        self.assertIn((-4, -1), a)

    def test_area_does_not_contain_coordinate(self):
        a = Area()
        test_map = {
            (0, 0): '_',
            (0, 1): '*',
            (-1, 0): ' ',
            (-1, -1): ' ',
            (-4, -1): ' ',
            (-5, -1): ' ',
            (-6, -1): ' ',
            (-1, 7): ' ',
        }
        a._data = test_map
        self.assertNotIn((4, 1), a)
