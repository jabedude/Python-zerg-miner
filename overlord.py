#!/usr/bin/env python3
'''This module implements the Overlord class'''

from mining.zerg import Zerg
from mining.drone.drone import Drone
from mining.area import Area
from mining.dashboard import Dashboard
from mining.pathfind.path import (
        area_to_graph,
        shortest_path,
        generate_cardinality
)


class Overlord(Zerg):
    '''
    The Overlord class spawns, deploys, and picks up Drones. It is responsible for
    sending drones a path to a mineral patch to mine.
    '''

    maps = dict()

    def __init__(self, ticks, refined_minerals):
        super().__init__()
        self.map_list = list()
        self.zerg_list = list()
        self.ticks = ticks
        self.refined_minerals = refined_minerals
        self.zerg = dict()  # TODO: @property this
        while self.refined_minerals > 0:
            self.refined_minerals -= Drone.get_init_cost()
            z = Drone()
            self.zerg_list.append(id(z))
            self.zerg[id(z)] = z

    def add_map(self, map_id, summary):
        '''Adds an identifier for a map + (map mineral density, internal map)'''
        internal_map = Area()
        internal_map.map_id = map_id
        self.map_list.append(map_id)
        self.maps[map_id] = internal_map

    def action(self, context):
        '''
        Entry point of action for Overlord. Context not currently used.
        '''
        #print(str(list(self.maps.values())[0]))
        for unit in list(self.zerg.values()):
            if unit.status:
                unit.path_queue = self._generate_path(unit.current_map, unit.position.current)
                unit.status = False
            elif unit.returning:
                unit.returning = False
                return "RETURN {}".format(id(unit))
        if self.zerg_list and self.map_list:
            curr_zerg = self.zerg_list.pop(0)
            curr_map = self.map_list.pop(0)
            self.zerg[curr_zerg].current_map = self.maps[curr_map]
            return "DEPLOY {} {}".format(curr_zerg, curr_map)
        else:
            return 'NONE'

    def dashboard(self):
        '''Returns a Dashboard object with drone POV'''
        return Dashboard()

    def _generate_drones(self, refined_minerals):
        '''Calculate quantities of drones to create'''
        raise NotImplementedError

    def _generate_path(self, zerg_map, current_position):
        '''Calculate a path from a zerg map + position to a mineral field'''
        mineral_coord = zerg_map.find_tile("*")
        graph = area_to_graph(zerg_map, goal=mineral_coord)
        if not mineral_coord:
            coordinate_path = shortest_path(graph, current_position, (0, 0))
        else:
            coordinate_path = shortest_path(graph, current_position, mineral_coord)
            home_path = shortest_path(graph, mineral_coord, (0, 0))
        return generate_cardinality(coordinate_path)
