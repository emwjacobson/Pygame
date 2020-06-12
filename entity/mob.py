import pygame
import settings
from .baseentity import BaseEntity
import math
import random


class Mob(BaseEntity):
    def __init__(self, x=0, y=0, angle=0, speed=0):
        super().__init__()
        self._entity_surface = pygame.image.load(settings.TEXTURE_DIR + "player.png")
        self._x = x
        self._y = y
        # Angle is in degrees, 0 being to the right, moving clockwise
        self.set_angle(angle)
        self._speed = speed

    def handle_events(self, events):
        pass

    def update(self, micro, world):
        super().update(micro, world)
        self._angle += random.randint(-5, 5)
        dx = math.cos(math.radians(self._angle)) * self._speed
        dy = math.sin(math.radians(self._angle)) * self._speed
        self._x += dx * micro
        self._y += dy * micro

        if self._x + self._entity_surface.get_width() >= world._width:
            self.set_angle(180 - self._angle)
        elif self._x <= 0:
            self.set_angle(180 - self._angle)
        if self._y <= 0:
            self.set_angle(360 - self._angle)
        elif self._y + self._entity_surface.get_height() >= world._height:
            self.set_angle(360 - self._angle)

    def render(self, surface):
        surface.blit(self._entity_surface, (self._x, self._y))
