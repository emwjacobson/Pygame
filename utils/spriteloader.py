import pygame


class SpriteLoader:

    def __init__(self):
        pass

    def load_sheet(path, sprite_width, sprite_height, offset_x, offset_y, columns, rows, scale=1):
        """
        Loads sprites from a sprite sheet.
        Loads them top to bottom, left to right

        @param path to the image
        @param sprite_width width of a single sprite in pixels
        @param sprite_height height of a single sprite in pixels
        @param offset_x offset from left of image in pixels
        @param offset_y offset from top of image in pixels
        @param columns number of columns in sprite map
        @param rows number of rows in sprite map
        @param scale Scaling factor to scale the sprites. 1 is normal size, 2 is 2x as large, etc.
        @return
        """
        sprites = []

        sprite_map = pygame.image.load(path)
        for y in range(offset_y, offset_y + (sprite_height * rows), sprite_width):
            for x in range(offset_x, offset_x + (sprite_width * columns), sprite_width):
                sub = sprite_map.subsurface((x, y, sprite_width, sprite_height))
                sub = pygame.transform.scale(sub, (sub.get_width() * scale, sub.get_height() * scale))
                sprites.append(sub)

        return sprites
