#!/usr/bin/env python3

import unittest
import sys
sys.path.append("..")
from mining import Overlord


class TestOverlord(unittest.TestCase):

    def test_overlord_creation(self):
        o = Overlord(0, 0)
        self.assertIsInstance(o, Overlord)

    def test_overlord_default_health(self):
        o = Overlord(0, 0)
        self.assertEqual(o.health, 1)

    def test_overlord_add_map(self):
        map_id = 30000
        summary = 2.99
        o = Overlord(ticks=100, refined_minerals=54)
        o.add_map(map_id, summary)
        self.assertEqual(o.maps[30000], 2.99)
        self.assertEqual(Overlord.maps[30000], 2.99)

    def test_overlord_generate_drones(self):
        pass
