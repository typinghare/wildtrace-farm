import os

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

        # Debug font
        font_path = os.path.join(os.path.join(context.settings.assets_dir, "fonts/Menlo.ttc"))
        self.font = pygame.font.Font(font_path, 16)

    def print(self, message: str) -> None:
        """
        Prints a message on the screen.
        :param message: Message to print on the screen.
        """
        display = self.context.game.display
        debug_layer: Layer = display.get_layer("debug")
        text = self.font.render(message.__repr__(), True, (0xFF,) * 3)

        debug_layer.clear()
        debug_layer.blit(text, Vector2(16, 16))
