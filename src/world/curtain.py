"""
Curtain module
"""
from src.core.context import Context
from src.core.display import Layer
from src.core.common.methodical import CallbackNode
from src.world.context_module import ContextModule


class Curtain(ContextModule):
    """
    Curtain.
    """

    MIN_ALPHA = 0
    MAX_ALPHA = 255

    def __init__(self, context: Context):
        super().__init__(context)

        # Layer
        self.layer: Layer = Layer(context.display.size)

        # Alpha (0 is transparent, 1 is opaque)
        self.alpha: int = 0

        # Callback node
        self.callback_node: CallbackNode = CallbackNode()

        # Init
        self._init_layer()

    def _init_layer(self) -> None:
        """
        Initializes layer.
        """
        self.context.display.set_layer("curtain", self.layer)

    def fade_out(self, speed: int) -> CallbackNode:
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
                self.callback_node.invoke()

        self.context.loop_manager.once(10, count, fade)
        self.callback_node = CallbackNode()

        return self.callback_node

    def fade_in(self, speed: int) -> CallbackNode:
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
                self.callback_node.invoke()

        self.context.loop_manager.once(10, count, fade)
        self.callback_node = CallbackNode()

        return self.callback_node

    def update(self) -> None:
        """
        Updates the layer.
        """
        self.layer.surface.fill((0, 0, 0, self.alpha))

    def is_ongoing(self) -> bool:
        """
        Whether the curtain animation is ongoing.
        """
        return self.alpha != 0
