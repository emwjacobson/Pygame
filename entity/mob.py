import pygame
import settings
from .baseentity import BaseEntity
from worlds.baseworld import BaseWorld
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

    def update(self, micro, world: BaseWorld):
        super().update(micro, world)
        self._angle += random.randint(-5, 5)
        dx = math.cos(math.radians(self._angle)) * self._speed
        dy = math.sin(math.radians(self._angle)) * self._speed
        self._x += dx * micro
        self._y += dy * micro

        if self._x + self._entity_surface.get_width() >= world.get_width():
            self.set_angle(180 - self._angle)
            self._x = world.get_width() - self._entity_surface.get_width()
        elif self._x <= 0:
            self.set_angle(180 - self._angle)
            self._x = 0
        if self._y <= 0:
            self.set_angle(360 - self._angle)
            self._y = 0
        elif self._y + self._entity_surface.get_height() >= world.get_height():
            self.set_angle(360 - self._angle)
            self._y = world.get_height() - self._entity_surface.get_height()

    def render(self, surface: pygame.Surface):
        if self._x < 0 or self._x > surface.get_width() or self._y < 0 or self._y > surface.get_height():
            return
        surface.blit(self._entity_surface, (self._x, self._y))
