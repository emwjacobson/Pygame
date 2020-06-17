import pygame


class BaseEntity(pygame.sprite.DirtySprite):
    image: pygame.Surface
    rect: pygame.Rect
    _speed: int
    _angle: int
    _sprite_map: pygame.Surface
    _counter: float
    rect: pygame.Rect
    image: pygame.Surface

    def __init__(self, rect, angle=0, speed=0, max_speed=100):
        super().__init__()
        """Initializes a new BaseEntity.

        Args:
            pos (list, optional): Starting position of the entity relative to the world. Defaults to [0, 0].
            angle (int, optional): Angle that the entity is facing. 0 is to the right, and rotates clockwise. Defaults to 0.
            speed (int, optional): Speed that the entity is moving. Defaults to 0.
        """
        self.rect = rect
        self.set_angle(angle)
        self._speed = speed
        self._counter = 0
        self._max_speed = max_speed
        self.dirty = 2

    def get_x(self):
        """Gets the x position of the entity, relative to the world

        Returns:
            int: The x position of the entity
        """
        return self.rect.x

    def get_y(self):
        """Gets the y position of the entity, relative to the world

        Returns:
            int: The y position of the entity
        """
        return self.rect.y

    def set_x(self, x):
        """Sets the x position of the entity, relative to the world

        Args:
            x (int): The x position of the entity
        """
        self.rect.x = x

    def add_x(self, x):
        """Adds `x` to the current x position

        Args:
            x (int): The amount to add to current x
        """
        self.rect.x += x

    def set_y(self, y):
        """Sets the y position of the entity, relative to the world

        Args:
            y (int): The y position of the entity
        """
        self.rect.y = y

    def add_y(self, y):
        """Adds `y` to the current y position

        Args:
            y (int): The amount to add to current y
        """
        self.rect.y += y

    def get_width(self):
        """Gets the width of the entity in pixels

        Returns:
            int: Width of the entity in pixels
        """
        return self.rect.width

    def get_height(self):
        """Gets the height of the entity in pixels

        Returns:
            int: Height of the entity in pixels
        """
        return self.rect.height

    def get_pos(self):
        """Gets the x, y position of the entity, relative to the world

        Returns:
            list[int]: The x, y position of the entity
        """
        return self.rect.topleft

    def set_speed(self, speed):
        """Gets the speed of the entity

        Args:
            speed (int): The speed to set the entity to
        """
        self._speed = speed

    def set_angle(self, angle):
        """Sets the angle that the entity is moving at

        Args:
            angle (int): The angle in degrees
        """
        self._angle = angle % 360

    def get_angle(self):
        """Get the angle in degrees of the entity

        Returns:
            int: The angle the entity is facing in degrees
        """
        return self._angle

    def handle_events(self, events, world):
        """Handles events for an entity.

        Args:
            events (list[pygame.event.Event]): A list of pygame Events
            world (BaseWorld): The world that the entity belongs to
        """
        pass

    def update(self, micro, world):
        """Updates the entity. Micro is passed to make different FPSs behave the same.

        Args:
            micro (float): Time in seconds that the last frame too.
            world (BaseWorld): The world that the entity belongs to
        """
        self._counter += micro
