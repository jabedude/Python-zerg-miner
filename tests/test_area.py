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

    def test_area_string(self):
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
