import pygame
import settings
from typing import List
from entity.baseentity import BaseEntity


class BaseWorld:
    _width: int
    _height: int
    _pos: [int]
    _entities: pygame.sprite.LayeredDirty()
    _player: BaseEntity
    _background_surface: pygame.Surface
    # _entity_surface = pygame.Surface

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
        self._entities = pygame.sprite.LayeredDirty()
        self._player = None
        self._counter = 0
        self._background_surface = pygame.Surface((self._width, self._height), flags=pygame.SRCALPHA | pygame.HWSURFACE | pygame.ASYNCBLIT | pygame.DOUBLEBUF)
        # self._entity_surface = pygame.Surface((self._width, self._height), flags=pygame.SRCALPHA | pygame.HWSURFACE | pygame.ASYNCBLIT | pygame.DOUBLEBUF)
        self._f_world = pygame.Surface((self._width, self._height), flags=pygame.SRCALPHA | pygame.HWSURFACE | pygame.ASYNCBLIT | pygame.DOUBLEBUF)
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

    def get_screen_pos(self, entity):
        """Gets the position of a given entity relative to the upper left corner of the screen

        Args:
            entity (BaseEntity): The entity to get position of

        Returns:
            list[int]: The [x, y] position of the sprite relative to upper left of the screen
        """
        return [self._pos[i] + entity.get_pos()[i] for i in range(2)]

    def to_world_pos(self, pos):
        """Converts a position relative to the screen to a position in the world

        Args:
            pos ([int]): [x, y] position relative to the screen
        """
        return [pos[i] - self._pos[i] for i in range(2)]

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
        self._counter += micro
        self._entities.update(micro, self)

    def render(self, screen: pygame.Surface):
        """Renders the world. Starts with the background_surface then the entity_surface over top.

        Args:
            screen (pygame.Surface): The surface for the world to be rendered to
        """
        self._f_world.blit(self._background_surface, (0, 0))
        self._entities.draw(self._f_world)

        # This implementation only draws the portion of the screen thats is visible to `screen`.
        # I didn't notice and improved performance, so I'll use the original way or rendering.
        # screen.blit(self._f_world, (0, 0), area=pygame.Rect([-i for i in self._pos], (settings.WIDTH, settings.HEIGHT)))

        # This implementation draws the entire world to the screen, with most of it not being visible.
        screen.blit(self._f_world, self._pos)
