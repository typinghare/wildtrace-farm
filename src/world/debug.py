import pygame.font
from pygame import Vector2

from src.core.context import Context
from src.core.display import Layer


class Debug:
    """
    Debug tool.
    """

    def __init__(self, context: Context):
        # Game context
        self.context: Context = context

        # Debug font
        self.font = pygame.font.Font(None, 16)

    def print(self, message: str) -> None:
        """
        Prints a message on the screen.
        :param message: Message to print on the screen.
        """
        display = self.context.game.display
        debug_layer: Layer = display.get_layer("debug")
        text = self.font.render(message, True, (0, 0, 0))

        debug_layer.clear()
        debug_layer.blit(text, Vector2(8, 8))
