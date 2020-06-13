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

    def __init__(self, pos=[0, 0]):
        super().__init__(pos, 90, 0, 150)

        self._sprite_map = SpriteLoader.load_sheet(settings.TEXTURE_DIR + "characters.png", 16, 16, 48, 0, 3, 4, 3)

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
                    self._max_speed += 50
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
                    self._max_speed -= 50

    def update(self, micro, world):
        super().update(micro, world)

        # ad	speed = 0		angle = _
        # ws	speed = 0		angle = _
        # wasd  speed = 0		angle = _
        #       speed = 0       angle = _

        # d	    speed = 100		angle = 0
        # wsd	speed = 100		angle = 0

        # sd	speed = 100		angle = 45

        # asd	speed = 100		angle = 90
        # s 	speed = 100		angle = 90

        # as	speed = 100		angle = 135

        # a	    speed = 100		angle = 180
        # was	speed = 100		angle = 180

        # wa	speed = 100		angle = 225

        # w	    speed = 100		angle = 270
        # wad	speed = 100		angle = 270

        # wd	speed = 100		angle = 315

        # TODO: Find a better way to do this...
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

        if self._angle > 315 or self._angle <= 45:
            self._cur_dir = self.Positons.RIGHT
        elif self._angle > 225 and self._angle <= 315:
            self._cur_dir = self.Positons.UP
        elif self._angle > 135 and self._angle <= 225:
            self._cur_dir = self.Positons.LEFT
        else:
            self._cur_dir = self.Positons.DOWN

        dx = math.cos(math.radians(self._angle)) * self._speed
        dy = math.sin(math.radians(self._angle)) * self._speed
        self._pos[0] += dx * micro
        self._pos[1] += dy * micro

        # Check boundries on the world, if they hit one then bounce off
        if self.get_x() + self._sprite_map[0].get_width() >= world.get_width():
            self.set_x(world.get_width() - self.get_width())
        elif self.get_x() <= 0:
            self.set_x(0)
        if self.get_y() <= 0:
            self.set_y(0)
        elif self.get_y() + self._sprite_map[0].get_height() >= world.get_height():
            self.set_y(world.get_height() - self.get_height())

    def render(self, surface: pygame.Surface):
        super().render(surface)

        surface.blit(self._sprite_map[self._cur_dir.value + self._cur_dir_mod], self._pos)
