import pygame
import settings
from .baseworld import BaseWorld
from entity.skeleton import BaseEntity, Skeleton
import random
import math


class DirtWorld(BaseWorld):
    def __init__(self, width=500, height=500, pos=(0, 0)):
        super().__init__(width, height, pos)

    def init_background(self):
        background_texture = pygame.image.load(settings.TEXTURE_DIR + "dirt.png")
        for x in range(0, self._width, background_texture.get_width()):
            for y in range(0, self._height, background_texture.get_height()):
                self._background_surface.blit(background_texture, (x, y))

    def populate_world(self):
        for i in range(50):
            self._entities.append(Skeleton(random.randint(50, self._width - 50), random.randint(80, self._height - 80),
                                  random.randint(0, 360), random.randint(100, 150)))
