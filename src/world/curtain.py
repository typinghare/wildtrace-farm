"""
Curtain module
"""
from typing import Callable

from src.core.context import Context
from src.core.display import Layer
from src.core.loop import Loop


class Curtain:
    """
    Curtain.
    """

    MIN_ALPHA = 0
    MAX_ALPHA = 255

    def __init__(self, context: Context):
        # Game context
        self.context: Context = context

        # Layer
        self.layer: Layer = Layer(context.display.size)

        # Alpha
        self.alpha: int = 0

        # Init
        self._init_layer()

    def _init_layer(self) -> None:
        """
        Initializes layer.
        """
        self.context.display.set_layer("curtain", self.layer)

    def fade_out(self, speed: int, callback: Callable[[], None] | None = None) -> None:
        """
        Fades out.
        :param: The speed to fade out.
        :param: The callback function to be called after the fade out.
        """
        self.alpha = 0
        count: int = int(Curtain.MAX_ALPHA / speed) + 1

        def fade(index: int) -> None:
            self.alpha = index * speed

            if index == count - 1:
                self.alpha = Curtain.MAX_ALPHA
                if callback is not None:
                    callback()

        self.context.loop_manager.once(10, count, fade)

    def fade_in(self, speed: int, callback: Callable[[], None] | None = None) -> None:
        """
        Fades in.
        :param: The speed to fade out.
        :param: The callback function to be called after the fade out.
        """
        self.alpha = 255
        count: int = int(Curtain.MAX_ALPHA / speed) + 1

        def fade(index: int) -> None:
            self.alpha = Curtain.MAX_ALPHA - index * speed

            if index == count - 1:
                self.alpha = Curtain.MIN_ALPHA
                if callback is not None:
                    callback()

        self.context.loop_manager.once(10, count, fade)

    def update(self) -> None:
        """
        Updates the layer.
        """
        self.layer.surface.fill((0, 0, 0, self.alpha))

    def is_ongoing(self) -> bool:
        """
        Whether the curtain animation is ongoing.
        """
