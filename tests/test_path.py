#!/usr/bin/env python3

import unittest
import sys
sys.path.append("..")
from pathfind import path


class TestPath(unittest.TestCase):

    def test_linear_distance(self):
        one = (-2, 1)
        two = (1, 5)
        distance = path.linear_distance(one, two)
        self.assertEqual(distance, 5)
