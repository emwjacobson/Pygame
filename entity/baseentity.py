import pygame


class BaseEntity:
    _pos: list
    _speed: int
    _angle: int
    _sprite_map: pygame.Surface
    _counter: float

    def __init__(self, pos=[0, 0], angle=0, speed=0, max_speed=100):
        """Initializes a new BaseEntity.

        Args:
            pos (list, optional): Starting position of the entity relative to the world. Defaults to [0, 0].
            angle (int, optional): Angle that the entity is facing. 0 is to the right, and rotates clockwise. Defaults to 0.
            speed (int, optional): Speed that the entity is moving. Defaults to 0.
        """
        self._pos = pos
        self.set_angle(angle)
        self._speed = speed
        self._counter = 0
        self._sprite_map = None
        self._max_speed = max_speed

    def get_x(self):
        """Gets the x position of the entity, relative to the world

        Returns:
            int: The x position of the entity
        """
        return self._pos[0]

    def get_y(self):
        """Gets the y position of the entity, relative to the world

        Returns:
            int: The y position of the entity
        """
        return self._pos[1]

    def set_x(self, x):
        """Sets the x position of the entity, relative to the world

        Args:
            x (int): The x position of the entity
        """
        self._pos[0] = x

    def set_y(self, y):
        """Sets the y position of the entity, relative to the world

        Args:
            y (int): The y position of the entity
        """
        self._pos[1] = y

    def get_width(self):
        """Gets the width of the entity in pixels

        Returns:
            int: Width of the entity in pixels
        """
        return self._sprite_map[0].get_width()

    def get_height(self):
        """Gets the height of the entity in pixels

        Returns:
            int: Height of the entity in pixels
        """
        return self._sprite_map[0].get_height()

    def get_pos(self):
        """Gets the x, y position of the entity, relative to the world

        Returns:
            list[int]: The x, y position of the entity
        """
        return self._pos

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

    def render(self, surface: pygame.Surface):
        """Renders the entity to a given surface

        Args:
            surface (pygame.Surface): The surface to render the entity to
        """
        pass
