"""
Scene manager module.
"""

from typing import Type, Callable

from pygame import Vector2

from src.core.common import Size
from src.core.context import Context
from src.world.camera import Camera
from src.world.map import Map, MapController


class SceneManager:
    """
    Scene manager serves as an essential class to manage map controllers and handles the transitions
    between scenes.
    """

    def __init__(self, context: Context):
        # Game context
        self.context: Context = context

        # Map controllers
        self._map_controller_map = {}

        # Current map
        self.current_map: Type[Map] | None = None

        # Current controller
        self.controller: MapController | None = None

    def load_map(self, map_to_load: Map) -> MapController:
        """
        Loads a map.
        :param map_to_load: The map to load.
        """
        map_class = map_to_load.__class__
        controller = self._map_controller_map.get(map_class)

        if controller is None:
            # Create a map controller if it does not exist
            controller = MapController(map_to_load, self.context)
            controller.load()
            controller.refresh_block_grid()
            self._map_controller_map[map_class] = controller

        return controller

    def change_map(self, map_to_change: Map, callback: Callable[[], None] | None = None) -> None:
        """
        Loads a map.
        :param map_to_change: The map to load.
        :param callback: Callback function that is called after the map is loaded.
        """
        self.current_map = map_to_change.__class__
        self.controller = self.load_map(map_to_change)

        # Set the map's layers to the display module
        self.controller.set_layers_to_display()

        # Camera
        screen_size = self.context.display.size
        map_size = self.controller.map.size
        cell_size = self.context.settings.display_cell_size
        self.context["camera"] = Camera(
            screen_size,
            Size(map_size.width * cell_size.width, map_size.height * cell_size.height),
        )

        # If the map is smaller than the screen, move it to the center of the screen
        camera: Camera = self.context["camera"]
        screen_size = self.context.display.size
        map_size = camera.map_size
        offset = Vector2(screen_size.width - map_size.width, screen_size.height - map_size.height)
        offset.x = max(offset.x // 2, 0)
        offset.y = max(offset.y // 2, 0)
        self.controller.set_offset(offset)

        if callback is not None:
            callback()

    def update_scene(self) -> None:
        """
        Updates current scene.
        """
        # Update the rect
        camera: Camera = self.context["camera"]
        rect = camera.get_screen_rect()
        self.controller.set_rect(rect)

    def is_map(self, _map: Map) -> bool:
        """
        Checks the current map.
        """
        return self.current_map == _map.__class__

    def get_map_controller(self, _map: Map) -> MapController:
        """
        Gets a map controller.
        """
        map_class = _map.__class__
        if map_class not in self._map_controller_map:
            self.load_map(_map)

        return self._map_controller_map[_map.__class__]
