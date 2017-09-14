#!/usr/bin/env python3

class Location:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.current = (x, y)
        self.east = (x + 1, y)
        self.west = (x - 1, y)
        self.north = (x, x + 1)
        self.south = (x, x - 1)
