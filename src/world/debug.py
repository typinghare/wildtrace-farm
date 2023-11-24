import os
from typing import Any

import pygame.font
from pygame import Vector2

from src.core.context import Context
from src.core.display import Layer


class Debug:
    """
    Debug tool.
    """

    INSTANCE: "Debug" = None

    def __init__(self, context: Context):
        # Game context
        self.context: Context = context

        # Font size
        self._font_size: int = 16

        # Debug font
        font_path = os.path.join(os.path.join(context.settings.assets_dir, "fonts/Menlo.ttc"))
        self.font = pygame.font.Font(font_path, self._font_size)

    def print(self, message: Any) -> None:
        """
        Prints a message on the screen.
        :param message: Message to print on the screen.
        """
        text = message.__repr__()
        if isinstance(text, tuple):
            text = f"tuple({message[0]}, {message[1]})"
        elif isinstance(text, Vector2):
            text = f"Vector2({message.x}, {message.y})"

        display = self.context.game.display
        debug_layer: Layer = display.get_layer("debug")

        debug_layer.clear()
        debug_layer.blit(
            self.font.render(text, True, (0xFF,) * 3), Vector2(self._font_size, self._font_size)
        )
