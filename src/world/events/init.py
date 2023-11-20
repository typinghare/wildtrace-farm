"""
Initialized events.
"""
from src.core import Size
from src.core.context import Context
from src.core.display import Layer, GridLayer
from src.world.debug import Debug


def init_layer(context: Context) -> None:
    """
    Initializes layers.
    """
    display = context.game.display
    settings = context.game.settings
    window_size = Size(display.screen.get_width(), display.screen.get_height())

    ground_layer = GridLayer("ground", settings.display_grid_size, settings.display_cell_size)
    character_layer = Layer("character", window_size)
    debug_layer = Layer("debug", window_size)

    display.add_layer(ground_layer)
    display.add_layer(character_layer)
    display.add_layer(debug_layer)


def init_debug(context: Context) -> None:
    """
    Initializes debug tool.
    """
    # Adds debug tool to context.
    context.set("debug", Debug(context))
