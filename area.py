#!/usr/bin/env python3

class Area:

    def __init__(self, *args):
        self._data = dict(args)

    def __setitem__(self, coordinates, tile):
        self._data[coordinates] = tile

    def __getitem__(self, coordinates):
        tile = self._data[coordinates]
        return tile

    def update(self, drone_position, context):
        self._data[drone_position] = 'Z'
        self._data[(drone_position[0], drone_position[1] + 1)] = context.north
        self._data[(drone_position[0] + 1, drone_position[1])] = context.west
        self._data[(drone_position[0] - 1, drone_position[1])] = context.east
        self._data[(drone_position[0], drone_position[1] - 1)] = context.south

    def __str__(self):
        # TODO: @property these attributes
        data = list(self._data.keys())
        min_x = min(data, key=lambda x: x[0], default=(0,0))[0]
        min_y = min(data, key=lambda x: x[1], default=(0,0))[1]
        max_x = max(data, key=lambda x: x[0], default=(0,0))[0]
        max_y = max(data, key=lambda x: x[1], default=(0,0))[1]

        ret = ''
        for y_coord in range(int(min_y), int(max_y) + 1):
            for x_coord in range(int(min_x), int(max_x) + 1):
                ret += "{} ".format(self._data.get((x_coord, y_coord), "?"))
            ret += '\n'

        return ret
