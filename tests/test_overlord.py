#!/usr/bin/env python3

import unittest


class TestOverlord(unittest.TestCase):
    
    def test_overlord_creation(self):
        o = Overlord()
        self.assertIsInstance(o, Overlord)
