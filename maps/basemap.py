import pygame
import settings


class BaseMap:
    background_texture: pygame.Surface
    background_surface: pygame.Surface

    def __init__(self):
        self.background_texture = pygame.image.load(settings.TEXTURE_DIR + "dirt.png")
        self.background_surface = pygame.Surface((settings.WIDTH, settings.HEIGHT))
        for x in range(0, settings.WIDTH, 32):
            for y in range(0, settings.HEIGHT, 32):
                self.background_surface.blit(self.background_texture, (x, y))

    def render(self, screen, events):
        screen.blit(self.background_surface, (0, 0))
