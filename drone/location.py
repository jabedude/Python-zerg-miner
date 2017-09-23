#!/usr/bin/env python3
'''This module implements the Location class'''


class Location:
    '''
    The Location class is used by Drone units to store their current and
    adjacent locations
    '''

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    @property
    def current(self):
        return (self.x, self.y)

    @current.setter
    def current(self, coords):
        self.x, self.y = coords

    @property
    def east(self):
        return (self.x + 1, self.y)

    @property
    def west(self):
        return (self.x - 1, self.y)

    @property
    def north(self):
        return (self.x, self.y + 1)

    @property
    def south(self):
        return (self.x, self.y - 1)
