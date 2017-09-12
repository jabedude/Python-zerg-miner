#!/usr/bin/env python3

from .zerg import Zerg


class Drone(Zerg):
    def __init__(self, health=40, capacity=10, moves=1):
        super().__init__()
        self.health = health
        self.capacity = capacity
        self.moves = moves

    def action(self, context):
        '''
        Entry point of action for Overlord. Context not currently used.
        '''
        pass
