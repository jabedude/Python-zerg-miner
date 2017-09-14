#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Zerg(ABC):

    def __init__(self):
        self.health = 1

    @abstractmethod
    def action(self):
        pass
