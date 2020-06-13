import pygame
import settings
from .baseentity import BaseEntity
from worlds.baseworld import BaseWorld
import math
import time
import random
from utils.spriteloader import SpriteLoader
from enum import Enum


class Skeleton(BaseEntity):
    class Positons(Enum):
        DOWN = 1
        LEFT = 4
        RIGHT = 7
        UP = 10

    def __init__(self, x=0, y=0, angle=0, speed=0):
        super().__init__(x, y, angle, speed)
        self._sprite_map = SpriteLoader.load_sheet(settings.TEXTURE_DIR + "characters.png", 16, 16, 144, 0, 3, 4, 2)
        self._cur_dir = self.Positons.DOWN
        self._cur_dir_mod = 0

    def update(self, micro, world: BaseWorld):
        super().update(micro, world)
        self._angle += random.randint(-5, 5)
        dx = math.cos(math.radians(self._angle)) * self._speed
        dy = math.sin(math.radians(self._angle)) * self._speed
        self._x += dx * micro
        self._y += dy * micro

        if self._x + self._sprite_map[0].get_width() >= world.get_width():
            self.set_angle(180 - self._angle)
            self._x = world.get_width() - self._sprite_map[0].get_width()
        elif self._x <= 0:
            self.set_angle(180 - self._angle)
            self._x = 0
        if self._y <= 0:
            self.set_angle(360 - self._angle)
            self._y = 0
        elif self._y + self._sprite_map[0].get_height() >= world.get_height():
            self.set_angle(360 - self._angle)
            self._y = world.get_height() - self._sprite_map[0].get_height()

        if self._counter > 0.75:
            self._cur_dir_mod = -1
        elif self._counter > 0.5:
            self._cur_dir_mod = 0
        elif self._counter > 0.25:
            self._cur_dir_mod = 1
        else:
            self._cur_dir_mod = 0

        if self._angle > 315 or self._angle <= 45:
            self._cur_dir = self.Positons.RIGHT
        elif self._angle > 225 and self._angle <= 315:
            self._cur_dir = self.Positons.UP
        elif self._angle > 135 and self._angle <= 225:
            self._cur_dir = self.Positons.LEFT
        else:
            self._cur_dir = self.Positons.DOWN

    def render(self, surface: pygame.Surface):
        surface.blit(self._sprite_map[self._cur_dir.value + self._cur_dir_mod], (self._x, self._y))
