#!/usr/bin/env python3

from mining.zerg import Zerg
from mining.drone.drone import Drone
from mining.area import Area


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
        '''Adds an identifier for a map + (map mineral density, internal map)'''
        internal_map = Area()
        internal_map.map_id = map_id
        self.maps[map_id] = (summary, internal_map)

    def action(self, context):
        '''
        Entry point of action for Overlord. Context not currently used.
        '''
        print(str(list(self.maps.values())[0][1]))
        ### TEMP ###
        #import random
        #act = random.randint(0, 3)
        #if act == 0:
        #    return "RETURN {}".format(random.choice(list(self.zerg.keys())))
        #else:
        #    return "DEPLOY {} {}".format(random.choice(list(self.zerg.keys())),
        #            random.choice(list(self.maps.keys())))
        list(self.zerg.values())[0].current_map = list(self.maps.values())[0][1]  # TODO: fix this
        return "DEPLOY {} {}".format(list(self.zerg.keys())[0],
                list(self.maps.keys())[0])
        ### TEMP ###

    def _generate_drones(self, refined_minerals):
        '''Calculate quantities of drones to create'''
        raise NotImplementedError
