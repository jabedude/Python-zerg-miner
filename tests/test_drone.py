#!/usr/bin/env python3

import unittest
import sys
sys.path.append("..") # TODO: ask instuctor about this kludge
from mining import Drone


class TestDrone(unittest.TestCase):

    def test_drone_creation(self):
        d = Drone()
        self.assertIsInstance(d, Drone)

    def test_drone_base_attributes(self):
        d = Drone()
        self.assertEqual(d.health, 40)
        self.assertEqual(d.capacity, 10)
        self.assertEqual(d.moves, 1)

    def test_drone_steps_count(self):
        d = Drone()
        for _ in range(5):
            d.action(None) # TODO: might need to change this
        self.assertEqual(d.steps(), 5)

    def test_drone_get_init_cost(self):
        cost = Drone().get_init_cost()
        self.assertEqual(cost, 9)
