"""
Debug module.
"""

from typing import Any, Dict

from pygame import Vector2

from src.core.context import Context
from src.core.display import Layer
from src.world.util import get_font


class Debug:
    """
    Debug tool.
    """

    INSTANCE: "Debug" = None

    class Module:
        def __init__(self, name: str):
            # Module name
            self.name: str = name

            # Text buffer
            self.text: str = ""

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

            self.text = f"[{self.name}] {text}"

    def __init__(self, context: Context):
        # Game context
        self.context: Context = context

        # Modules
        self._by_name: Dict[str, Debug.Module] = {}

        # Font size
        self._font_size: int = 16

        # Debug font
        self.font = get_font(self._font_size, "menlo/Menlo.ttc")

    def print_all(self):
        debug_layer: Layer = self.context.display.get_layer("debug")
        debug_layer.clear()

        for i, module in enumerate(self._by_name.values()):
            offset = Vector2(self._font_size, self._font_size * (i + 1))
            text_surface = self.font.render(module.text, True, (0xFF,) * 3)
            debug_layer.blit(text_surface, offset)

    @staticmethod
    def get_module(name: str) -> "Debug.Module":
        """
        Returns a debug module.
        :param name: The name of the module.
        """
        self = Debug.INSTANCE

        if name in self._by_name:
            return self._by_name[name]

        module = Debug.Module(name)
        self._by_name[name] = module

        return module
