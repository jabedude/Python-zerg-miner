#!/usr/bin/env python3

from mining.zerg import Zerg
from mining.drone import Drone


class Overlord(Zerg):

    maps = dict()

    def __init__(self, ticks, refined_minerals):
        super().__init__()
        self.ticks = ticks
        self.refined_minerals = refined_minerals
        self.zerg = dict()  # TODO: @property this
        ### TEMP ###
        for _ in range(3):
            z = Drone()
            self.zerg[id(z)] = z
        ### TEMP ###

    def add_map(self, map_id, summary):
        '''Adds an identifier for a map and a summary of the map'''
        self.maps[map_id] = summary

    def action(self, context):
        '''
        Entry point of action for Overlord. Context not currently used.
        '''
        ### TEMP ###
        import random
        act = random.randint(0, 3)
        if act == 0:
            return "RETURN {}".format(random.choice(list(self.zerg.keys())))
        else:
            return "DEPLOY {} {}".format(random.choice(list(self.zerg.keys())),
                    random.choice(list(self.maps.keys())))
        ### TEMP ###

    def _generate_drones(self, refined_minerals):
        '''Calculate quantities of drones to create'''
        raise NotImplementedError
