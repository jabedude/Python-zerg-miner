#!/usr/bin/env python3

from .zerg import Zerg


class Overlord(Zerg):
    def __init__(self, ticks, refined_minerals):
        super().__init__()
        self.ticks = ticks
        self.refined_minerals = refined_minerals
        self.maps = dict()
        self.zerg = dict() # TODO: @property this

    def add_map(self, map_id, summary):
        '''Adds an identifier for a map and a summary of the map'''
        pass

    def action(self, context):
        '''
        Entry point of action for Overlord. Context not currently used.
        '''
        pass
