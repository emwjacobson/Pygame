import pygame
import math
from .baseentity import BaseEntity
from utils.spriteloader import SpriteLoader
import settings


class Player(BaseEntity):
    def __init__(self, pos=[0, 0], angle=0, speed=0):
        super().__init__(pos, angle, speed)

        self._sprite_map = SpriteLoader.load_sheet(settings.TEXTURE_DIR + "characters.png", 16, 16, 48, 0, 3, 4, 5)

        self._move_right = False
        self._move_left = False
        self._move_up = False
        self._move_down = False

    def handle_events(self, events, world):
        super().handle_events(events, world)

        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_a:
                    self._move_left = True
                elif e.key == pygame.K_d:
                    self._move_right = True
                elif e.key == pygame.K_w:
                    self._move_up = True
                elif e.key == pygame.K_s:
                    self._move_down = True
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_a:
                    self._move_left = False
                elif e.key == pygame.K_d:
                    self._move_right = False
                elif e.key == pygame.K_w:
                    self._move_up = False
                elif e.key == pygame.K_s:
                    self._move_down = False

    def update(self, micro, world):
        super().handle_events(micro, world)

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

        w, a, s, d = self._move_up, self._move_left, self._move_down, self._move_right

        if (not w and a and not s and d) or (w and not a and s and not d) or (w and a and s and d) or (not w and not a and not s and not d):
            self._speed = 0
        else:
            self._speed = 100
            if (not w and not a and not s and d) or (w and not a and s and d):
                self._angle = 0
            elif (not w and not a and s and d):
                self._angle = 45
            elif (not w and a and s and d) or (not w and not a and s and not d):
                self._angle = 90
            elif (not w and a and s and not d):
                self._angle = 135
            elif (not w and a and not s and not d) or (w and a and s and not d):
                self._angle = 180
            elif (w and a and not s and not d):
                self._angle = 225
            elif (w and not a and not s and not d) or (w and a and not s and d):
                self._angle = 270
            elif (w and not a and not s and d):
                self._angle = 315

        dx = math.cos(math.radians(self._angle)) * self._speed
        dy = math.sin(math.radians(self._angle)) * self._speed
        self._pos[0] += dx * micro
        self._pos[1] += dy * micro

    def render(self, surface: pygame.Surface):
        super().render(surface)

        surface.blit(self._sprite_map[1], self._pos)

