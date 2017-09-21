#!/usr/bin/env python3

import unittest
from mining.drone.location import Location


class TestLocation(unittest.TestCase):

    def test_location_creation(self):
        l = Location(0, 0)
        self.assertIsInstance(l, Location)

    def test_location_east(self):
        l = Location()
        self.assertEqual((1, 0), l.east)

    def test_location_west(self):
        l = Location()
        self.assertEqual((-1, 0), l.west)

    def test_location_north(self):
        l = Location()
        self.assertEqual((0, 1), l.north)

    def test_location_south(self):
        l = Location()
        self.assertEqual((0, -1), l.south)

    def test_location_current(self):
        l = Location(9, 9)
        self.assertEqual((9, 9), l.current)
