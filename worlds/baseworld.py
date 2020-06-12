import pygame
import settings
from typing import List


class BaseWorld:
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

    def update(self, micro):
        pass

    def render(self, screen):
        pass
