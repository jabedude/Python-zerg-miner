#!/usr/bin/env python3

import unittest
from mining.dashboard import Dashboard
from mining.area import Area


class TestDashboard(unittest.TestCase):

    def test_dashboard_creation(self):
        db = Dashboard()
        self.assertIsInstance(db, Dashboard)

    def test_dashboard_representation(self):
        a1 = Area()
        a2 = Area()
        a3 = Area()
        l = [a1, a2, a3]
        db = Dashboard(l)
        expected = '''? 
==============================
? 
==============================
? 
'''
        self.assertEqual(expected, str(db))

    def test_dashboard_maps_have_data(self):
        a1 = Area()
        a2 = Area()
        a3 = Area()
        test_map = {
            (0, 0): '_',
            (0, 1): '*',
            (-1, 0): '#',
            (-1, -1): '#',
            (1, 0): '#',
            (1, 1): '#',
        }
        a1._data = a2._data = a3._data = test_map
        l = [a1, a2, a3]
        db = Dashboard(l)
        expected = '''# ? ? 
# _ # 
? * # 
==============================
# ? ? 
# _ # 
? * # 
==============================
# ? ? 
# _ # 
? * # 
'''
        self.assertEqual(expected, str(db))
