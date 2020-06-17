import pygame
import settings
from .baseworld import BaseWorld
from utils.spriteloader import SpriteLoader
from entity import BaseEntity, Player, Skeleton
import random
import math


class DirtWorld(BaseWorld):
    def __init__(self, width=500, height=500, pos=[0, 0]):
        self._seed = "PyGaMe"
        super().__init__(width, height, pos)

    def init_background(self):
        gen = random.Random()
        gen.seed(self._seed)

        sprite_map = SpriteLoader.load_sheet(settings.TEXTURE_DIR + "basictiles.png", 16, 16, 0, 0, 8, 13)
        grass = sprite_map[11]
        flowers = sprite_map[12]
        tree = sprite_map[30]
        stone = sprite_map[58]
        for x in range(0, self._width, sprite_map[0].get_width()):
            for y in range(0, self._height, sprite_map[0].get_height()):
                self._background_surface.blit(grass, (x, y))
                rand = gen.randint(0, 100)
                # TODO: Make a dictionary that will handle spawn percentages
                # [{icon: surface, pct: 10}, ...]
                if rand in [0, 1, 2, 3, 4, 5]:
                    self._background_surface.blit(flowers, (x, y))
                elif rand in [6]:
                    self._background_surface.blit(tree, (x, y))
                elif rand in [7]:
                    self._background_surface.blit(stone, (x, y))

    def populate_world(self):
        # Skeleton Sprites
        # for i in range(100):
        #     self._entities.add(Skeleton([random.randint(50, self._width - 50), random.randint(80, self._height - 80)],
        #                        random.randint(0, 360), 0, random.randint(50, 80)))

        # Player
        self._player = Player([settings.WIDTH, settings.HEIGHT])
        self._entities.add(self._player)

    def handle_events(self, events):
        super().handle_events(events)
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                self._entities.add(Skeleton(self.to_world_pos(e.pos), random.randint(0, 359), 0, random.randint(50, 80)))

    def update(self, micro):
        super().update(micro)

        p_pos = self.get_screen_pos(self._player)
        if p_pos[0] < 250:
            self._pos[0] = self._pos[0] + (250 - p_pos[0])
        elif p_pos[0] + self._player.get_width() > settings.WIDTH - 250:
            self._pos[0] = self._pos[0] - ((p_pos[0] + self._player.get_width()) - (settings.WIDTH - 250))

        if p_pos[1] < 150:
            self._pos[1] = self._pos[1] + (150 - p_pos[1])
        elif p_pos[1] + self._player.get_height() > settings.HEIGHT - 150:
            self._pos[1] = self._pos[1] - ((p_pos[1] + self._player.get_height()) - (settings.HEIGHT - 150))
