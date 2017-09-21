#!/usr/bin/env python3

import unittest
import sys
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
