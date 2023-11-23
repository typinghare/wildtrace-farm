"""
Initialized events.
"""
from src.core.common import Size
from src.core.context import Context
from src.core.display import Layer
from src.world.camera import Camera
from src.world.data.maps import Maps
from src.world.debug import Debug
from src.world.map import MapController


def init_map(context: Context) -> None:
    """
    Initializes map.
    """
    # initialize character layer
    screen_size = context.settings.display_window_size
    context.display.unshift_layer("character", Layer(screen_size))

    # Map controller
    map_controller = MapController(Maps.Home, context)
    map_controller.load(context)
    context["map_controller"] = map_controller

    # Camera
    map_size = map_controller.map.size
    cell_size = context.settings.display_cell_size
    camera = Camera(
        screen_size, Size(map_size.width * cell_size.width, map_size.height * cell_size.height)
    )
    context["camera"] = camera


def init_debug(context: Context) -> None:
    """
    Initializes the debug tool.
    """
    context["debug"] = Debug.INSTANCE = Debug(context)
