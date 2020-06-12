import pygame
import settings
from .baseworld import BaseWorld
from entity.mob import BaseEntity, Mob
import random
import math


class DirtWorld(BaseWorld):
    def __init__(self, width=500, height=500):
        self._width = width
        self._height = height
        self._x = 0
        self._y = 0
        self._dx = 0
        self._dy = 0
        self._entities = []

        self.map_surface = pygame.Surface((self._width, self._height))
        self.player_surface = pygame.Surface((self._width, self._height), flags=pygame.SRCALPHA)
        self.init_background()
        self.populate_map()

    def init_background(self):
        background_texture = pygame.image.load(settings.TEXTURE_DIR + "dirt.png")
        for x in range(0, self._width, background_texture.get_width()):
            for y in range(0, self._height, background_texture.get_height()):
                self.map_surface.blit(background_texture, (x, y))

    def populate_map(self):
        for i in range(1):
            self._entities.append(Mob(random.randint(50, self._width - 50), random.randint(80, self._height - 80),
                                      random.randint(0, 360), 100))

    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_a:
                    self._dx = 100
                elif e.key == pygame.K_d:
                    self._dx = -100

                if e.key == pygame.K_w:
                    self._dy = 100
                elif e.key == pygame.K_s:
                    self._dy = -100
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_a:
                    if pygame.key.get_pressed()[pygame.K_d]:
                        self._dx = -100
                    else:
                        self._dx = 0
                elif e.key == pygame.K_d:
                    if pygame.key.get_pressed()[pygame.K_a]:
                        self._dx = 100
                    else:
                        self._dx = 0

                if e.key == pygame.K_w:
                    if pygame.key.get_pressed()[pygame.K_s]:
                        self._dy = -100
                    else:
                        self._dy = 0
                elif e.key == pygame.K_s:
                    if pygame.key.get_pressed()[pygame.K_w]:
                        self._dy = 100
                    else:
                        self._dy = 0

    def update(self, micro):
        self._x += self._dx * micro
        self._y += self._dy * micro

        e: BaseEntity
        for e in self._entities:
            e.update(micro, self)

    def render(self, screen):
        # Render map background
        screen.blit(self.map_surface, (self._x, self._y))

        # Render entities
        self.player_surface.fill((0, 0, 0, 0))
        for e in self._entities:
            e.render(self.player_surface)

        screen.blit(self.player_surface, (self._x, self._y))