"""
Message box module.
"""
import os

from pygame import Vector2, Rect, font

from src.core.common import Size
from src.core.context import Context
from src.core.display import Layer
from src.core.loop import LoopManager, Loop


class MessageBox:
    """
    Message box.
    """

    def __init__(self, context: Context):
        # Game context
        self.context = context

        # Message to display; the message box will be hidden if the message is None
        self.message: str | None = None

        # Message buffer
        self.message_buffer: str = ""

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

        # Loop
        self.loop: Loop | None = None

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
        self.message_buffer = message
        message_len = len(message)
        loop_manager: LoopManager = self.context.loop_manager

        def forward(index: int) -> None:
            self.message = message[0:index]

            if index == message_len:
                loop_manager.remove(self.loop)

        self.loop = loop_manager.register(15, message_len + 1, forward)

    def stop_playing(self) -> None:
        """
        Stops the loop and display the whole message right away.
        """
        # Stop the loop
        if self.loop is not None:
            loop_manager: LoopManager = self.context.loop_manager
            loop_manager.remove(self.loop)
            self.loop = None

        # Flush the buffer
        self.message = self.message_buffer

    def hide(self) -> None:
        """
        Hides the message box; clears the buffer.
        """
        self.stop_playing()
        self.message = None
        self.message_buffer = ""

    def update(self) -> None:
        """
        Updates the message box layer.
        """
        if self.message is None:
            self.layer.hidden = True
        else:
            self.layer.hidden = False
            text = self.font.render(self.message, True, (0x33,) * 3)
            self.layer.surface.blit(text, self.margin)

    def is_displayed(self) -> None:
        """
        Whether the message box is being displayed.
        """
        return self.message is not None
