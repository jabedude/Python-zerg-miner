#!/usr/bin/env python3

import unittest
from unittest import mock
import sys
sys.path.append("..")
from drone import Scout


class TestScout(unittest.TestCase):

    def test_scout_creation(self):
        s = Scout()
        self.assertIsInstance(s, Scout)

    def test_scout_base_attributes(self):
        s = Scout()
        self.assertEqual(s.health, 20)
        self.assertEqual(s.capacity, 5)
        self.assertEqual(s.moves, 3)

    def test_scout_get_init_cost(self):
        cost = Scout().get_init_cost()
        self.assertEqual(cost, 12)
