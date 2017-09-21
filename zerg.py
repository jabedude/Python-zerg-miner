#!/usr/bin/env python3
'''Module implements the abstract Zerg class'''

from abc import ABC, abstractmethod


class Zerg(ABC):
    '''Abstract bass class from which Drones + Overlords inherit from'''

    def __init__(self):
        self.health = 1

    @abstractmethod
    def action(self):
        pass
