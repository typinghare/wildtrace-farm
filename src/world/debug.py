import os
from typing import Any, Dict

import pygame.font
from pygame import Vector2

from src.core.context import Context
from src.core.display import Layer


class Debug:
    """
    Debug tool.
    """

    INSTANCE: "Debug" = None

    class Module:
        def __init__(self, context: Context, name: str):
            # Game context
            self.context: Context = context

            # Module name
            self.name = name

            # Font size
            self._font_size: int = 16

            # Debug font
            font_path = os.path.join(os.path.join(context.settings.assets_dir, "fonts/Menlo.ttc"))
            self.font = pygame.font.Font(font_path, self._font_size)

        def print(self, message: Any, description: str = "") -> None:
            """
            Prints a message on the screen.
            :param message: Message to print on the screen.
            :param description: Description.
            """
            text = message.__repr__()
            if isinstance(text, tuple):
                text = f"tuple({message[0]}, {message[1]})"
            elif isinstance(text, Vector2):
                text = f"Vector2({message.x}, {message.y})"

            if description:
                text = description + ": " + text

            text = f"[{self.name}] {text}"

            debug_layer: Layer = self.context.display.get_layer("debug")
            debug_layer.clear()
            debug_layer.blit(
                self.font.render(text, True, (0xFF,) * 3), Vector2(self._font_size, self._font_size)
            )

    def __init__(self, context: Context):
        # Game context
        self.context: Context = context

        # Modules
        self._by_name: Dict[str, Debug.Module] = {}

    def get_module(self, name: str) -> "Debug.Module":
        """
        Returns a debug module.
        :param name: The name of the module.
        """

        if name in self._by_name:
            return self._by_name[name]

        module = Debug.Module(self.context, name)
        self._by_name[name] = module

        return module
