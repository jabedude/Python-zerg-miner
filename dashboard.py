#!/usr/bin/env python3
'''Module implements the Dashboard class'''


class Dashboard:
    '''Dashboard represents the aggregate of Drone units' maps'''

    def __init__(self, map_list=None):
        self._data = map_list

    def __str__(self):
        delim = "=" * 30 + '\n'
        ret = "{}".format(delim.join(map(str, self._data)))
        return ret
