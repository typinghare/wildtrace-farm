"""
Map crafting events.
"""
from pygame import Vector2

from src.core.context import Context
from src.core.display import GridLayer
from src.world.camera import Camera
from src.world.map import MapController


def update_map(context: Context) -> None:
    """
    Updates the map.
    """

    map_controller: MapController = context["map_controller"]
    camera: Camera = context["camera"]

    # If the map is smaller than the screen, move it to the center of the screen
    screen_size = camera.screen_size
    map_size = camera.map_size
    offset = Vector2(screen_size.width - map_size.width, screen_size.height - map_size.height)
    offset.x = max(offset.x // 2, 0)
    offset.y = max(offset.y // 2, 0)
    map_controller.set_offset(offset)

    # Update the rect
    rect = camera.get_screen_rect()
    map_controller.set_rect(rect)

    # Update character layer
    character_layer: GridLayer = context.display.get_layer("character")
    virtual_center = camera.get_virtual_center()
    character_layer.offset = Vector2(virtual_center[0], virtual_center[1])
