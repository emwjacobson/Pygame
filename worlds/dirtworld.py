import pygame
import settings
from .baseworld import BaseWorld
from entity.skeleton import BaseEntity, Skeleton
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
        self._pan_speed = 300
        self._zoom = 1

        self.map_surface = pygame.Surface((self._width, self._height))
        self.entity_surface = pygame.Surface((self._width, self._height), flags=pygame.SRCALPHA)
        self.init_background()
        self.populate_map()

    def init_background(self):
        background_texture = pygame.image.load(settings.TEXTURE_DIR + "dirt.png")
        for x in range(0, self._width, background_texture.get_width()):
            for y in range(0, self._height, background_texture.get_height()):
                self.map_surface.blit(background_texture, (x, y))

    def populate_map(self):
        for i in range(50):
            self._entities.append(Skeleton(random.randint(50, self._width - 50), random.randint(80, self._height - 80),
                                  random.randint(0, 360), random.randint(100, 150)))

    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                # Handle Pan controls
                if e.key == pygame.K_a:
                    self._dx = self._pan_speed
                elif e.key == pygame.K_d:
                    self._dx = -self._pan_speed

                elif e.key == pygame.K_w:
                    self._dy = self._pan_speed
                elif e.key == pygame.K_s:
                    self._dy = -self._pan_speed

                # Pan speed
                elif e.key == pygame.K_PAGEUP:
                    self._pan_speed += 100
                elif e.key == pygame.K_PAGEDOWN:
                    self._pan_speed -= 100

                # Zoom
                # Zooming is a bit funky, as it will zoom based on the upper
                # left area of the surface, so need to adjust the x and y
                elif e.key == pygame.K_LEFTBRACKET and self._zoom < 2:
                    self._zoom += 0.1
                    # new_x = self._width * (self._zoom - 1) * 0.5
                    # self._x -= new_x
                    # new_y = self._height * (self._zoom - 1) * 0.5
                    # self._y -= new_y
                elif e.key == pygame.K_RIGHTBRACKET and self._zoom > 0.5:
                    self._zoom -= 0.1
                    # new_x = self._width * (self._zoom - 1) * 0.5
                    # self._x -= new_x
                    # new_y = self._height * (self._zoom - 1) * 0.5
                    # self._y -= new_y
            elif e.type == pygame.KEYUP:
                # Handle Pan controls
                if e.key == pygame.K_a:
                    if pygame.key.get_pressed()[pygame.K_d]:
                        self._dx = -self._pan_speed
                    else:
                        self._dx = 0
                elif e.key == pygame.K_d:
                    if pygame.key.get_pressed()[pygame.K_a]:
                        self._dx = self._pan_speed
                    else:
                        self._dx = 0

                elif e.key == pygame.K_w:
                    if pygame.key.get_pressed()[pygame.K_s]:
                        self._dy = -self._pan_speed
                    else:
                        self._dy = 0
                elif e.key == pygame.K_s:
                    if pygame.key.get_pressed()[pygame.K_w]:
                        self._dy = self._pan_speed
                    else:
                        self._dy = 0

    def update(self, micro):
        self._x += self._dx * micro
        self._y += self._dy * micro

        e: BaseEntity
        for e in self._entities:
            e.update(micro, self)

    def render(self, screen):
        f_world = pygame.Surface((self._width, self._height))

        # Render map background
        f_world.blit(self.map_surface, (0, 0))

        # Render entities
        self.entity_surface.fill((0, 0, 0, 0))
        for e in self._entities:
            e.render(self.entity_surface)

        f_world.blit(self.entity_surface, (0, 0))

        screen.blit(pygame.transform.scale(f_world, (int(self._width * self._zoom), int(self._height * self._zoom))), (self._x, self._y))
