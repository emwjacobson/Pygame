import pygame
# from worlds.baseworld import BaseWorld


class BaseEntity:
    _pos: list
    _speed: int
    _angle: int
    _entity_surface: pygame.Surface
    _counter: float

    def __init__(self, pos=[0, 0], angle=0, speed=0):
        self._pos = pos
        self._angle = angle
        self._speed = speed
        self._counter = 0

    def get_x(self):
        return self._pos[0]

    def get_y(self):
        return self._pos[1]

    def set_x(self, x):
        self._pos[0] = x

    def set_y(self, y):
        self._pos[1] = y

    def get_width(self):
        return self._entity_surface.get_width()

    def get_height(self):
        return self._entity_surface.get_height()

    def get_pos(self):
        return (self._x, self._y)

    def set_speed(self, speed):
        self._speed = speed

    def set_angle(self, angle):
        # TODO: Make this use modulo
        if angle < 0:
            self.set_angle(360 + angle)
        elif angle >= 360:
            self.set_angle(angle - 360)
        else:
            self._angle = angle

    def get_angle(self):
        return self._angle

    def handle_events(self, events, world):
        pass

    def update(self, micro, world):
        self._counter = (self._counter + micro) % 1

    def render(self, surface):
        pass

# ad	speed = 0		angle = _
# ws	speed = 0		angle = _
# wasd  speed = 0		angle = _

# w	    speed = 100		angle = 0
# wad	speed = 100		angle = 0

# wd	speed = 100		angle = 45

# d	    speed = 100		angle = 90
# wsd	speed = 100		angle = 90

# sd	speed = 100		angle = 135

# asd	speed = 100		angle = 180
# s 	speed = 100		angle = 180

# as	speed = 100		angle = 225

# a	    speed = 100		angle = 270
# was	speed = 100		angle = 270

# wa	speed = 100		angle = 315
