"""
Map crafting events.
"""
from pygame import Vector2

from src.core.context import Context
from src.world.camera import Camera
from src.world.map import MapController


def update_map(context: Context) -> None:
    """
    Updates the map.
    """

    map_controller: MapController = context["map_controller"]
    camera: Camera = context["camera"]

    # If the map is less than the screen, align it to center
    screen_size = camera.screen_size
    map_size = camera.map_size
    rect = camera.get_screen_rect()
    offset = Vector2(screen_size.width - map_size.width, screen_size.height - map_size.height)
    if offset.x > 0:
        offset.x //= 2
    if offset.y > 0:
        offset.y //= 2

    if offset.x < 0:
        offset.x = rect.x
    if offset.y < 0:
        offset.y = rect.y

    map_controller.set_offset(offset)
