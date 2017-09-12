#!/usr/bin/env python3

from .zerg import Zerg


class Drone(Zerg):

    health = 40
    capacity = 10
    moves = 1

    def __init__(self):
        self.step_count = 0

    def action(self, context):
        '''
        Entry point of action for Overlord. Context not currently used.
        '''
        self.step_count += 1
        pass

    def steps(self):
        '''Return the number of steps taken by drone'''
        return self.step_count

    @classmethod
    def get_init_cost(cls):
        minerals = cls.health / 10
        minerals += cls.capacity / 5
        minerals += cls.moves * 3
        return minerals
