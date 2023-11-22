"""
Camera module.
"""
from typing import Tuple

from pygame import Vector2, Rect

from src.core.common import Size
from src.core.constant import Direction


class Camera:
    """
    Camera.
    """

    def __init__(self, screen_size: Size, layer_size: Size):
        # The screen size
        self.screen_size: Size = screen_size

        # The layer size
        self.layer_size: Size = layer_size

        # Offset
        self.offset: Vector2 = Vector2(0, 0)

    def move(self, direction: Direction, distance: float) -> None:
        """
        Moves the camera frame towards certain direction.
        :param direction: The direction to move towards.
        :param distance: The distance to move.
        """
        if direction == Direction.UP:
            self.offset.y -= distance
        elif direction == Direction.RIGHT:
            self.offset.x += distance
        elif direction == Direction.DOWN:
            self.offset.y += distance
        elif direction == Direction.LEFT:
            self.offset.x -= distance

    def get_screen_rect(self) -> Rect:
        """
        Returns the rectangle of the real screen.
        """
        x = min(max(self.offset.x, 0), self.layer_size.width - self.screen_size.width)
        y = min(max(self.offset.y, 0), self.layer_size.height - self.screen_size.height)

        return Rect(x, y, self.screen_size.width, self.screen_size.height)

    def get_virtual_center(self) -> Tuple[int, int]:
        """
        Returns the center of the virtual screen.
        """
        return (
            (self.offset.x + self.screen_size.width) / 2,
            (self.offset.y + self.screen_size.height) / 2,
        )