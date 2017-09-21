#!/usr/bin/env python3

import unittest
import sys
sys.path.append("..")
from dashboard import Dashboard


class TestDashboard(unittest.TestCase):

    def test_dashboard_creation(self):
        db = Dashboard()
        self.assertIsInstance(db, Dashboard)
