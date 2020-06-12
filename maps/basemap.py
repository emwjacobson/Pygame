import pygame
import settings
from typing import List


class BaseMap:
    _width: int
    _height: int
    _x: int
    _y: int

    def __init__(self):
        pass

    def init_background(self):
        pass

    def handle_events(self, events):
        pass

    def render(self, micro, screen):
        pass
