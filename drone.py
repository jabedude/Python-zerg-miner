#!/usr/bin/env python3

from mining.zerg import Zerg
import mining

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
        self.current_position = (0, 0)
        self.path_queue = None  # TODO: list() of path (actions)

    def action(self, context):
        '''
        Entry point of action for Overlord. Context not currently used.
        '''
        self.step_count += 1
        mining.Overlord.maps[self.current_map][1].update(self.current_position, context)
        ### TEMP ###
        import random
        act = random.randint(0, 3)
        if act == 0 and context.north == ' ':
            self.current_position = (self.current_position[0], self.current_position[1] + 1)
            return 'NORTH'
        elif act == 1 and context.south == ' ':
            self.current_position = (self.current_position[0], self.current_position[1] - 1)
            return 'SOUTH'
        elif act == 2 and context.east == ' ':
            self.current_position = (self.current_position[0] - 1, self.current_position[1])
            return 'EAST'
        elif act == 3 and context.west == ' ':
            self.current_position = (self.current_position[0] + 1, self.current_position[1])
            return 'WEST'
        else:
            return 'CENTER'
        ### TEMP ###

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
