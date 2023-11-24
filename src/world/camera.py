"""
Camera module.
"""
from typing import Tuple

from pygame import Vector2, Rect

from src.core.common import Size


class Camera:
    """
    Camera.
    """

    def __init__(self, screen_size: Size, map_size: Size):
        # The size of the screen
        self.screen_size: Size = screen_size

        # The size of the map
        self.map_size: Size = map_size

        # Offset
        self.offset: Vector2 = Vector2(0, 0)

    def move(self, displacement: Vector2) -> None:
        """
        Moves the camera frame towards certain direction.
        :param displacement: The displacement to move
        """
        self.offset += displacement

    def get_screen_rect(self) -> Rect:
        """
        Returns the rectangle of the real screen.
        """
        pos = [0, 0]

        # x
        if self.screen_size.width < self.map_size.width:
            pos[0] = min(max(self.offset.x, 0), self.map_size.width - self.screen_size.width)
        else:
            pos[0] = 0

        # y
        if self.screen_size.height < self.map_size.height:
            pos[1] = min(max(self.offset.y, 0), self.map_size.height - self.screen_size.height)
        else:
            pos[1] = 0

        return Rect(pos[0], pos[1], self.screen_size.width, self.screen_size.height)

    def get_virtual_center(self) -> Tuple[int, int]:
        """
        Returns the center of the virtual screen.
        """
        return (
            (self.offset.x + self.screen_size.width) / 2,
            (self.offset.y + self.screen_size.height) / 2,
        )
