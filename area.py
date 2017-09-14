#!/usr/bin/env python3

class Area:

    def __init__(self, *args):
        self._data = dict(args)
        self.map_id = None

    def __setitem__(self, coordinates, tile):
        self._data[coordinates] = tile

    def __getitem__(self, coordinates):
        tile = self._data[coordinates]
        return tile

    def update(self, position, context):
        self._data[position.current] = 'Z'
        self._data[position.north] = context.north
        self._data[position.west] = context.west
        self._data[position.east] = context.east
        self._data[position.south] = context.south

    def get(self, key):
        return self._data.get(key, "?")

    def __contains__(self, item):
        if isinstance(item, str):
            return item in list(self._data.values())
        else:
            return item in list(self._data.keys())

    def __str__(self):
        # TODO: @property these attributes
        print(self._data)
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
