#!/usr/bin/env python3

import unittest
import sys
sys.path.append("..") # TODO: ask instuctor about this kludge
from mining import Overlord


class TestOverlord(unittest.TestCase):

    def test_overlord_creation(self):
        o = Overlord(0, 0)
        self.assertIsInstance(o, Overlord)

    def test_overlord_default_health(self):
        o = Overlord(0, 0)
        self.assertEqual(o.health, 1)
