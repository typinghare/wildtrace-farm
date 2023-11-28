"""
Map crafting events.
"""
from pygame import Vector2

from src.core.common import Size
from src.core.context import Context
from src.world.camera import Camera
from src.world.data.maps import Maps
from src.world.map import MapController


def init_map(context: Context) -> None:
    """
    Initializes map.
    """
    # Map controller
    default_map = Maps.Farm
    context["map_controller"] = map_controller = MapController(default_map, context)
    map_controller.load(context)
    map_controller.refresh_block_grid()

    # Camera
    screen_size = context.display.size
    map_size = map_controller.map.size
    cell_size = context.settings.display_cell_size
    context["camera"] = Camera(
        screen_size,
        Size(map_size.width * cell_size.width, map_size.height * cell_size.height),
    )


def update_map(context: Context) -> None:
    """
    Updates the map.
    """

    map_controller: MapController = context["map_controller"]
    camera: Camera = context["camera"]

    # If the map is smaller than the screen, move it to the center of the screen
    screen_size = context.display.size
    map_size = camera.map_size
    offset = Vector2(screen_size.width - map_size.width, screen_size.height - map_size.height)
    offset.x = max(offset.x // 2, 0)
    offset.y = max(offset.y // 2, 0)
    map_controller.set_offset(offset)

    # Update the rect
    rect = camera.get_screen_rect()
    map_controller.set_rect(rect)
