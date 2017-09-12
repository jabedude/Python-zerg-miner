#!/usr/bin/env python3

from mining.zerg import Zerg


class Overlord(Zerg):
    def __init__(self, ticks, refined_minerals):
        super().__init__()
        self.ticks = ticks
        self.refined_minerals = refined_minerals
        self.maps = dict()
        self.zerg = dict() # TODO: @property this

    def add_map(self, map_id, summary):
        '''Adds an identifier for a map and a summary of the map'''
        self.maps[map_id] = summary

    def action(self, context):
        '''
        Entry point of action for Overlord. Context not currently used.
        '''
        pass

    def _generate_drones(self):
        '''Calculate quantities of drones to create'''
        raise NotImplementedError
