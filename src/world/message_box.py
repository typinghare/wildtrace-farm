"""
Message box module.
"""
import os

from pygame import Vector2, Rect, font

from src.core.common import Size
from src.core.context import Context
from src.core.display import Layer
from src.core.loop import LoopManager


class MessageBox:
    """
    Message box.
    """

    def __init__(self, context: Context):
        # Game context
        self.context = context

        # Message to display; the message box will be hidden if the message is None
        self.message: str | None = None

        # Size and offset
        screen_size = self.context.display.size
        self.size: Size = Size(screen_size.width * 0.9, screen_size.height * 0.3)
        self.offset: Vector2 = Vector2(
            (screen_size.width - self.size.width) // 2, screen_size.height * 0.65
        )

        # Thickness
        self.border_thickness: int = 3

        # Message box layer
        self.layer: Layer = Layer(self.size)

        # Font
        self.font_size: int = 24
        font_path = os.path.join(os.path.join(context.settings.assets_dir, "fonts/Menlo.ttc"))
        self.font = font.Font(font_path, self.font_size)

        # Margin offset
        self.margin = Vector2(0.03 * self.size.width, 0.1 * self.size.height)

        # Init
        self._init_layer()

    def _init_layer(self) -> None:
        """
        Initializes the layer.
        """
        self.context.display.set_layer("message_box", self.layer)
        self.layer.offset = self.offset

        self.layer.surface.fill("blue")
        rect = Rect(
            self.border_thickness,
            self.border_thickness,
            self.layer.size.width - self.border_thickness * 2,
            self.layer.size.height - self.border_thickness * 2,
        )
        self.layer.surface.fill("white", rect)

    def play(self, message: str) -> None:
        """
        Plays a message.
        :param message: The message to display.
        """
        message_len = len(message)
        loop_manager: LoopManager = self.context.loop_manager

        def forward(index: int) -> None:
            self.message = message[0:index]

            if index == message_len:
                loop_manager.remove(loop)

        loop = loop_manager.register(15, message_len + 1, forward)

    def update(self) -> None:
        """
        Updates the message box layer.
        """
        text = self.font.render(self.message, True, (0x33,) * 3)
        self.layer.surface.blit(text, self.margin)
