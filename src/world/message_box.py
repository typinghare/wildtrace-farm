"""
Message box module.
"""
from pygame import Vector2, Rect

from src.core.common import Size
from src.core.context import Context
from src.core.display import Layer
from src.core.loop import LoopManager, Loop
from src.core.common.methodical import CallbackNode
from src.world.context_module import ContextModule
from src.world.util import get_font


class MessageBox(ContextModule):
    """
    Message box.
    """

    def __init__(self, context: Context):
        super().__init__(context)

        # Message play speed
        self.play_speed: int = 25

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
        self.font = get_font(self.font_size, context.settings.message_box_font)
        self.hint_font = get_font(round(self.font_size * 0.75), context.settings.message_box_font)

        # Margin offset
        self.margin = Vector2(0.03 * self.size.width, 0.1 * self.size.height)

        # Loop
        self.loop: Loop | None = None

        # Callback
        self.callback_node: CallbackNode = CallbackNode()

        # Init
        self._init_layer()

    def _init_layer(self) -> None:
        """
        Initializes the layer.
        """
        self.context.display.set_layer("message_box", self.layer)
        self.layer.offset = self.offset

        self.layer.surface.fill("blue")
        self.clear_layer()

    def play(self, message: str) -> CallbackNode:
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
                self.stop_playing()

        self.loop = loop_manager.loop(self.play_speed, message_len + 1, forward)
        self.callback_node = CallbackNode()

        return self.callback_node

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
        self.clear_layer()

        # Invoke the callback node
        self.callback_node.invoke()

    def update(self) -> None:
        """
        Updates the message box layer.
        """
        if self.message is None:
            self.layer.hidden = True
        else:
            self.layer.hidden = False
            lines = self.message.split("\n")
            for i, line in enumerate(lines):
                text = self.font.render(line, True, (0x33,) * 3)
                line_margin = Vector2(self.margin.x, self.margin.y + self.font_size * 1.3 * i)
                self.layer.surface.blit(text, line_margin)

        # Write hint ("Press [J] to continue...")
        text = self.hint_font.render("Press [J] to continue ..", True, (0x33,) * 3)
        self.layer.blit(text, Vector2(self.size.width - 300, self.size.height - 30))

    def clear_layer(self) -> None:
        """
        Clears all words in the layer.
        """
        rect = Rect(
            self.border_thickness,
            self.border_thickness,
            self.layer.size.width - self.border_thickness * 2,
            self.layer.size.height - self.border_thickness * 2,
        )
        self.layer.surface.fill("white", rect)

    def is_displayed(self) -> None:
        """
        Whether the message box is being displayed.
        """
        return self.message is not None
