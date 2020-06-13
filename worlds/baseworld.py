import pygame
import settings
from typing import List


class BaseWorld:
    _width: int
    _height: int
    _x: int
    _y: int

    def __init__(self, width=500, height=500, pos=[0, 0]):
        """Initializes a new BaseWorld. Worlds are made up of 2 layers, a
        background surface and an entity surface. Like it sounds, background
        textures go on the background_surface, and entities on the entity_surface.

        Args:
            width (int, optional): The width of the world. Defaults to 500.
            height (int, optional): The height of the world. Defaults to 500.
            x (int, optional): The starting position, relative to the upper left of the window. Defaults to [0, 0].
        """
        self._width = width
        self._height = height
        self._pos = pos
        self._entities = []
        self._background_surface = pygame.Surface((self._width, self._height))
        self._entity_surface = pygame.Surface((self._width, self._height), flags=pygame.SRCALPHA)
        self.init_background()
        self.populate_world()

    def init_background(self):
        """Overload this function in a subclass to populate the background_surface.
        """
        pass

    def populate_world(self):
        """Overload this function in a subclass to populate the world with entities
        """
        pass

    def get_width(self):
        """Gets the width of the current world

        Returns:
            int: Width, in pixels, of the world
        """
        return self._width

    def get_height(self):
        """Gets the height of the current world

        Returns:
            int: Height, in pixels, of the world
        """
        return self._height

    def get_entities(self):
        """Gets the entities in the current world

        Returns:
            list[BaseEntity]: A list of BaseEntity objects in the world
        """
        return self._entities

    def handle_events(self, events):
        """Handles the events for the world, also calls handle_events for every entity in the world

        Args:
            events (list[pygame.event.Event]): A list of pygame events
        """
        for e in self._entities:
            e.handle_events(events, self)

    def update(self, micro):
        """Update all entities

        Args:
            micro (float): Number of seconds that it took to render the frame. Used to make any FPS run at the same speed.
        """
        for e in self._entities:
            e.update(micro, self)

    def render(self, screen: pygame.Surface):
        """Renders the world. Starts with the background_surface then the entity_surface over top.

        Args:
            screen (pygame.Surface): The surface for the world to be rendered to
        """
        f_world = pygame.Surface((self._width, self._height))

        # Render map background
        f_world.blit(self._background_surface, (0, 0))

        # Render entities
        self._entity_surface.fill((0, 0, 0, 0))
        for e in self._entities:
            e.render(self._entity_surface)

        f_world.blit(self._entity_surface, (0, 0))

        screen.blit(f_world, self._pos)
