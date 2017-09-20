#!/usr/bin/env python3

from mining.zerg import Zerg
from mining.drone.drone import Drone
from mining.area import Area
from mining.pathfind.path import (
        area_to_graph,
        shortest_path,
        generate_cardinality
)


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
        for unit in list(self.zerg.values()):
            if unit.status:
                unit.path_queue = self._generate_path(unit.current_map, unit.position.current)
                unit.status = False
            elif unit.returning:
                return "RETURN {}".format(id(unit))
        #if act == 0:
        #    return "RETURN {}".format(random.choice(list(self.zerg.keys())))
        #else:
        #    return "DEPLOY {} {}".format(random.choice(list(self.zerg.keys())),
        #            random.choice(list(self.maps.keys())))
        list(self.zerg.values())[0].current_map = list(self.maps.values())[0][1]  # TODO: fix this
        return "DEPLOY {} {}".format(list(self.zerg.keys())[0],
                list(self.maps.keys())[0])

    def _generate_drones(self, refined_minerals):
        '''Calculate quantities of drones to create'''
        raise NotImplementedError

    def _generate_path(self, zerg_map, current_position):
        mineral_coord = zerg_map.find_tile("*")
        # TODO: if no min_coord, return HOME
        graph = area_to_graph(zerg_map, goal=mineral_coord)
        if not mineral_coord:
            coordinate_path = shortest_path(graph, current_position, (0, 0))
        else:
            coordinate_path = shortest_path(graph, current_position, mineral_coord)
            home_path = shortest_path(graph, mineral_coord, (0, 0))
        print(coordinate_path)
        return generate_cardinality(coordinate_path)
