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

    def __init__(self, pos=(0, 0), angle=0, speed=0, max_speed=100):
        super().__init__(pos, angle, speed, max_speed)
        self._sprite_map = SpriteLoader.load_sheet(settings.TEXTURE_DIR + "characters.png", 16, 16, 144, 0, 3, 4, 2)
        self._cur_dir = self.Positons.DOWN
        self._cur_dir_mod = 0
        self._random_wait = (random.random() * 15) + 5          # [5, 15)
        self._random_wait_sec = (random.random() * 2) + 0.25    # [0.25, 2.25)

    def update(self, micro, world: BaseWorld):
        super().update(micro, world)

        # Apply a random angle to make then walk in more than straight lines
        self._angle += random.randint(-5, 5)
        dx = math.cos(math.radians(self._angle)) * self._speed
        dy = math.sin(math.radians(self._angle)) * self._speed
        self._pos[0] += dx * micro
        self._pos[1] += dy * micro

        # Check boundries on the world, if they hit one then bounce off
        if self.get_x() + self._sprite_map[0].get_width() >= world.get_width():
            self.set_angle(180 - self._angle)
            self.set_x(world.get_width() - self._sprite_map[0].get_width())
        elif self.get_x() <= 0:
            self.set_angle(180 - self._angle)
            self.set_x(0)
        if self.get_y() <= 0:
            self.set_angle(360 - self._angle)
            self.set_y(0)
        elif self.get_y() + self._sprite_map[0].get_height() >= world.get_height():
            self.set_angle(360 - self._angle)
            self.set_y(world.get_height() - self._sprite_map[0].get_height())

        # Control the animation based on time
        c = self._counter % 1
        if self._speed == 0:
            self._cur_dir_mod = 0
        elif c > 0.75:
            self._cur_dir_mod = -1
        elif c > 0.5:
            self._cur_dir_mod = 0
        elif c > 0.25:
            self._cur_dir_mod = 1
        else:
            self._cur_dir_mod = 0

        # Make this sprite stop moving for 2 second every _random_wait seconds
        if self._counter > self._random_wait and self._counter % self._random_wait <= self._random_wait_sec:
            self._speed = 0
        else:
            self._speed = self._max_speed

        # Set the current direction based on current angle
        if self._angle > 315 or self._angle <= 45:
            self._cur_dir = self.Positons.RIGHT
        elif self._angle > 225 and self._angle <= 315:
            self._cur_dir = self.Positons.UP
        elif self._angle > 135 and self._angle <= 225:
            self._cur_dir = self.Positons.LEFT
        else:
            self._cur_dir = self.Positons.DOWN

    def render(self, surface: pygame.Surface):
        surface.blit(self._sprite_map[self._cur_dir.value + self._cur_dir_mod], self._pos)
