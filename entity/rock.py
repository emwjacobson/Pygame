from .baseentity import BaseEntity
import pygame
from utils.spriteloader import SpriteLoader
import settings


class Rock(BaseEntity):
    def __init__(self, pos, angle, speed):
        self._sprite_map = SpriteLoader.load_sheet(settings.TEXTURE_DIR + "basictiles.png", 7, 6, 41, 112, 1, 1, 2)
        super().__init__(pygame.Rect(pos, (self._sprite_map[0].get_width(), self._sprite_map[0].get_height())), angle, speed, speed)
        self.image = self._sprite_map[0]

    def update(self, micro, world):
        super().update(micro, world)
        if self._counter > 5:
            self.kill()
