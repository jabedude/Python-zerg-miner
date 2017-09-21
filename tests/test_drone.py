#!/usr/bin/env python3

import unittest
from unittest import mock
from mining.drone.drone import Drone, Miner


class TestDrone(unittest.TestCase):

    def test_drone_creation(self):
        d = Drone()
        self.assertIsInstance(d, Drone)

    def test_drone_base_attributes(self):
        d = Drone()
        self.assertEqual(d.health, 40)
        self.assertEqual(d.capacity, 10)
        self.assertEqual(d.moves, 1)

    def test_drone_get_init_cost(self):
        cost = Drone().get_init_cost()
        self.assertEqual(cost, 9)

    def test_miner_get_init_cost(self):
        cost = Miner().get_init_cost()
        self.assertEqual(cost, 7)
