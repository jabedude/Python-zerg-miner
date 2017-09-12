#!/usr/bin/env python3

#from mining import Zerg
from .zerg import Zerg

class Overlord(Zerg):
    def __init__(self, ticks, refined_minerals):
        super().__init__()
        self.ticks = ticks
        self.refined_minerals = refined_minerals

    def action(self):
        pass
