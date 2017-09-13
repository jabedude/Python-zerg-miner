#!/usr/bin/env python3

import unittest
from unittest import mock
import sys
sys.path.append("..")
from drone import Drone, Miner


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
        mock_Context = mock.Mock()
        mock_Context.north = mock_Context.south = mock_Context.east = mock_Context.west = '*'
        d = Drone()
        for _ in range(5):
            d.action(mock_Context)  # TODO: might need to change this
        self.assertEqual(d.steps(), 5)

    def test_drone_get_init_cost(self):
        cost = Drone().get_init_cost()
        self.assertEqual(cost, 9)

    def test_miner_get_init_cost(self):
        cost = Miner().get_init_cost()
        self.assertEqual(cost, 7)
