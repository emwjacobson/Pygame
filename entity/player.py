import pygame
import math
from .baseentity import BaseEntity
from utils.spriteloader import SpriteLoader
import settings
from enum import Enum


class Player(BaseEntity):
    class Positons(Enum):
        DOWN = 1
        LEFT = 4
        RIGHT = 7
        UP = 10

    def __init__(self, pos):
        self._sprite_map = SpriteLoader.load_sheet(settings.TEXTURE_DIR + "characters.png", 16, 16, 48, 0, 3, 4, 3)
        super().__init__(pygame.Rect(pos, (self._sprite_map[0].get_width(), self._sprite_map[0].get_height())), 90, 0, 150)

        self._move_right = False
        self._move_left = False
        self._move_up = False
        self._move_down = False
        self._cur_dir = self.Positons.DOWN
        self._cur_dir_mod = 0

    def handle_events(self, events, world):
        super().handle_events(events, world)

        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == settings.MOVE_LEFT:
                    self._move_left = True
                elif e.key == settings.MOVE_RIGHT:
                    self._move_right = True
                elif e.key == settings.MOVE_UP:
                    self._move_up = True
                elif e.key == settings.MOVE_DOWN:
                    self._move_down = True
                elif e.key == pygame.K_SPACE:
                    self._max_speed += 100
            elif e.type == pygame.KEYUP:
                if e.key == settings.MOVE_LEFT:
                    self._move_left = False
                elif e.key == settings.MOVE_RIGHT:
                    self._move_right = False
                elif e.key == settings.MOVE_UP:
                    self._move_up = False
                elif e.key == settings.MOVE_DOWN:
                    self._move_down = False
                elif e.key == pygame.K_SPACE:
                    self._max_speed -= 100

    def update(self, micro, world):
        super().update(micro, world)

        # TODO: Find a better way to do this...
        # Get which keys are pressed to determine direction
        w, a, s, d = self._move_up, self._move_left, self._move_down, self._move_right

        if (not w and a and not s and d) or (w and not a and s and not d) or (w and a and s and d) or (not w and not a and not s and not d):
            self._speed = 0
        else:
            self._speed = self._max_speed
            if (not w and not a and not s and d) or (w and not a and s and d):
                self.set_angle(0)
            elif (not w and not a and s and d):
                self.set_angle(45)
            elif (not w and a and s and d) or (not w and not a and s and not d):
                self.set_angle(90)
            elif (not w and a and s and not d):
                self.set_angle(135)
            elif (not w and a and not s and not d) or (w and a and s and not d):
                self.set_angle(180)
            elif (w and a and not s and not d):
                self.set_angle(225)
            elif (w and not a and not s and not d) or (w and a and not s and d):
                self.set_angle(270)
            elif (w and not a and not s and d):
                self.set_angle(315)

        # Get the offset of the current direction
        c = self._counter % 0.5
        if self._speed == 0:
            self._cur_dir_mod = 0
        elif c > 0.125 * 3:
            self._cur_dir_mod = -1
        elif c > 0.125 * 2:
            self._cur_dir_mod = 0
        elif c > 0.125:
            self._cur_dir_mod = 1
        else:
            self._cur_dir_mod = 0

        # Determine direction of the sprite
        if self._angle > 315 or self._angle <= 45:
            self._cur_dir = self.Positons.RIGHT
        elif self._angle > 225 and self._angle <= 315:
            self._cur_dir = self.Positons.UP
        elif self._angle > 135 and self._angle <= 225:
            self._cur_dir = self.Positons.LEFT
        else:
            self._cur_dir = self.Positons.DOWN

        # Check boundries on the world, if they hit one then bounce off
        if self.get_x() + self.get_width() >= world.get_width():
            self.set_x(world.get_width() - self.get_width())
        elif self.get_x() <= 0:
            self.set_x(0)
        if self.get_y() <= 0:
            self.set_y(0)
        elif self.get_y() + self.get_height() >= world.get_height():
            self.set_y(world.get_height() - self.get_height())

        self.image = self._sprite_map[self._cur_dir.value + self._cur_dir_mod]
