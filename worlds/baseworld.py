import pygame
import settings
from typing import List


class BaseWorld:
    _width: int
    _height: int
    _x: int
    _y: int

    def __init__(self, width=500, height=500, pos=(0, 0)):
        """Initializes a new BaseWorld. Worlds are made up of 2 layers, a
        background surface and an entity surface. Like it sounds, background
        textures go on the background_surface, and entities on the entity_surface.

        Args:
            width (int, optional): The width of the world. Defaults to 500.
            height (int, optional): The height of the world. Defaults to 500.
            x (int, optional): The starting x position, relative to the window. Defaults to 0.
        """
        # Initializes a new BaseWorld. Worlds are made up of 2 layers, a
        # background surface and a

        # @param width The width of the world
        # @param height The height of the world
        # @param x The initial x position of the world
        # @param y The initial y position of the world
        #
        self._width = width
        self._height = height
        self._x = pos[0]
        self._y = pos[1]
        self._entities = []
        self._background_surface = pygame.Surface((self._width, self._height))
        self._entity_surface = pygame.Surface((self._width, self._height), flags=pygame.SRCALPHA)
        self.init_background()
        self.populate_world()

    def init_background(self):
        """
        """
        pass

    def populate_world(self):
        pass

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_entities(self):
        return self._entities

    def handle_events(self, events):
        for e in self._entities:
            e.handle_events(events, self)

    def update(self, micro):
        for e in self._entities:
            e.update(micro, self)

    def render(self, screen):
        f_world = pygame.Surface((self._width, self._height))

        # Render map background
        f_world.blit(self._background_surface, (0, 0))

        # Render entities
        self._entity_surface.fill((0, 0, 0, 0))
        for e in self._entities:
            e.render(self._entity_surface)

        f_world.blit(self._entity_surface, (0, 0))

        screen.blit(f_world, (self._x, self._y))
