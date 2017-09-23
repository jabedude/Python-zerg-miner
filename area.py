#!/usr/bin/env python3
'''This module implements the Area class used by Drones'''


class Area:
    '''
    Area is the internal "map" used by drones and overlords to see their map
    '''

    def __init__(self, *args):
        self._data = dict(args)
        self.map_id = None
        self._explored = list((0, 0))

    def is_explored(self, coordinates):
        '''Returns a list of explored coordinates in the area'''
        return coordinates in self._explored

    def update(self, position, context):
        '''Update area data with new data from drone'''
        self._explored.append(position.current)
        self._data[position.current] = 'Z'
        self._data[position.north] = context.north
        self._data[position.west] = context.west
        self._data[position.east] = context.east
        self._data[position.south] = context.south

    def get(self, key):
        '''Return the tile at coordinate 'key'. Defaults to "?"'''
        return self._data.get(key, "?")

    def find_tile(self, tile):
        for coord, area_tile in self._data.items():
            if area_tile == tile:
                return coord

    def __setitem__(self, coordinates, tile):
        self._data[coordinates] = tile

    def __getitem__(self, coordinates):
        tile = self._data.get(coordinates, "?")
        return tile

    def __contains__(self, item):
        if isinstance(item, str):
            return item in list(self._data.values())
        else:
            return item in list(self._data.keys())

    def __iter__(self):
        return iter(self._data)

    def __str__(self):
        # TODO: @property these attributes
        data = list(self._data.keys())
        min_x = min(data, key=lambda x: x[0], default=(0, 0))[0]
        min_y = min(data, key=lambda x: x[1], default=(0, 0))[1]
        max_x = max(data, key=lambda x: x[0], default=(0, 0))[0]
        max_y = max(data, key=lambda x: x[1], default=(0, 0))[1]

        ret = ''
        for y_coord in range(int(min_y), int(max_y) + 1):
            for x_coord in range(int(min_x), int(max_x) + 1):
                ret += "{} ".format(self._data.get((x_coord, y_coord), "?"))
            ret += '\n'

        return ret
