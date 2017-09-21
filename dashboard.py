#!/usr/bin/env python3


class Dashboard:

    def __init__(self, map_list=None):
        self._data = map_list

    def __str__(self):
        delim = "=" * 30 + '\n'
        ret = "{}".format(delim.join(map(str, self._data)))
        return ret
