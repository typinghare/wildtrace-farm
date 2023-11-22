"""
Initialized events.
"""
from src.core.context import Context
from src.core.display import Layer
from src.world.data.maps import Maps
from src.world.debug import Debug
from src.world.map import MapController


def init_layer(context: Context) -> None:
    """
    Initializes layers.
    """
    # initialize character layer
    screen_size = context.settings.display_window_size
    context.display.unshift_layer("character", Layer(screen_size))

    # Map controller
    map_controller = MapController(Maps.House, context)
    context["map_controller"] = map_controller
    map_controller.load(context)


def init_debug(context: Context) -> None:
    """
    Initializes debug tool.
    """
    # Adds debug tool to context.
    debug = Debug(context)
    context["debug"] = debug
    Debug.INSTANCE = debug
