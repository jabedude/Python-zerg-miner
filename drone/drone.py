#!/usr/bin/env python3

from mining.zerg import Zerg
import mining
from .location import Location
from mining.pathfind.path import (
        area_to_graph,
        shortest_path,
        generate_cardinality
)


class Drone(Zerg):

    health_points = 40
    carrying_capacity = 10
    move_count = 1

    def __init__(self):
        self.step_count = 0
        self.health = Drone.health_points
        self.capacity = Drone.carrying_capacity
        self.moves = Drone.move_count
        self.current_map = None
        self.position = Location(0, 0)
        self.status = False
        self.deployed = False
        self.returning = False
        self.pickup = False
        self.path_queue = None
        self.last_xy = None
        self.last_move = None

    @property
    def current_map(self):
        return self._current_map

    @current_map.setter
    def current_map(self, zerg_map):
        self._current_map = zerg_map
        self.deployed = True

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, cap):
        self._capacity = cap
        if self._capacity < 0:
            graph = area_to_graph(self.current_map)
            coords = shortest_path(graph, self.position.current, (0, 0))
            self.path_queue = generate_cardinality(coords)
            self.status = False
            self.returning = True

    def action(self, context):
        '''
        Entry point of action for Drone unit. Context information about surrounding tiles.
        '''
        #print(id(self))
        #print(self.path_queue)
        #print(self.returning)
        #print(self.status)
        if self.last_xy is not None and self.last_xy != (context.x, context.y):
            directions = {
                'NORTH': (0, 1),
                'SOUTH': (0, -1),
                'EAST': (1, 0),
                'WEST': (-1, 0)
            }
            move = directions[self.last_move]
            self.position.current = tuple(map(lambda x, y: x + y, self.position.current, move))
            self.step_count += 1
        elif (self.last_move is not None and self.path_queue is not None and
              self.last_xy == (context.x, context.y) and not self.returning):
            # Mining here
            self.capacity -= 1
            return self.last_move

        self.current_map.update(self.position, context)
        self.last_xy = (context.x, context.y)

        if not self.path_queue and not self.returning:
            if context.north == ' ' and not self.current_map.is_explored(self.position.north):
                self.last_move = 'NORTH'
                return 'NORTH'
            elif context.south == ' ' and not self.current_map.is_explored(self.position.south):
                self.last_move = 'SOUTH'
                return 'SOUTH'
            elif context.east == ' ' and not self.current_map.is_explored(self.position.east):
                self.last_move = 'EAST'
                return 'EAST'
            elif context.west == ' ' and not self.current_map.is_explored(self.position.west):
                self.last_move = 'WEST'
                return 'WEST'
            else:
                self.last_move = None
                #print("IDLE")
                self.status = True
                return 'CENTER'
        elif self.path_queue:
            #print(self.path_queue)
            if self.capacity < 0:
                self.returning = True
            self.last_move = self.path_queue[0]
            return self.path_queue.pop(0)
        else:
            self.status = False
            self.returning = False
            return 'CENTER'

    def steps(self):
        '''Return the number of steps taken by drone'''
        return self.step_count

    @classmethod
    def get_init_cost(cls):
        minerals = cls.health_points // 10
        minerals += cls.carrying_capacity // 5
        minerals += cls.move_count * 3
        return minerals


class Scout(Drone):

    health_points = 20
    carrying_capacity = 5
    move_count = 3

    def __init__(self):
        super().__init__()
        self.health = Scout.health_points
        self.capacity = Scout.carrying_capacity
        self.moves = Scout.move_count


class Miner(Drone):

    health_points = 10
    carrying_capacity = 15
    move_count = 1

    def __init__(self):
        super().__init__()
        self.health = Miner.health_points
        self.capacity = Miner.carrying_capacity
        self.moves = Miner.move_count
