#!/usr/bin/env python3

import unittest
import sys
sys.path.append("..") # TODO: ask instuctor about this kludge
from mining import Drone


class TestDrone(unittest.TestCase):

    def test_drone_creation(self):
        d = Drone()
        self.assertIsInstance(d, Drone)

    def test_drone_default_attributes(self):
        d = Drone()
        self.assertEqual(d.health, 40)
        self.assertEqual(d.capacity, 10)
        self.assertEqual(d.moves, 1)
