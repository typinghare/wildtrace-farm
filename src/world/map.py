"""
Map module
"""
from typing import Dict, List

from pygame import Surface, Rect

from src.core.common import Size
from src.core.settings import Settings
from src.core.common import CoordinateSet
from src.core.context import Context
from src.core.display import GridLayer
from src.world.data.frames import Frames
from src.world.renderer import HouseRenderer

settings = Settings()


class Map:
    """
    Map.
    """

    def __init__(self, size: Size):
        # The size of the map
        self.size = size

        # The layers
        self._layers: Dict[str, GridLayer] = {}

    def _init(self):
        self._layers["ground"] = GridLayer(self.size, settings.display_cell_size)
        self._layers["floor"] = GridLayer(self.size, settings.display_cell_size)
        self._layers["furniture_bottom"] = GridLayer(self.size, settings.display_cell_size)
        self._layers["furniture_top"] = GridLayer(self.size, settings.display_cell_size)

    def get_layer(self, name: str) -> GridLayer:
        """
        Gets a layer.
        :param name: The name of the layer.
        """
        return self._layers[name]

    def clone(self) -> "Map":
        """
        Returns a deep copy of this map.
        """
        _map = Map(self.size)
        for name, layer in self._layers.items():
            _map._layers[name] = layer.clone()

        return _map

    def load(self, context: Context) -> None:
        """
        Loads this map to the game.
        :param context: The game context.
        """

    def unload(self, context: Context) -> None:
        """
        Unloads this map from the game.
        :param context: The game context.
        """


class MapController:
    """
    Map controller.
    """

    def __init__(self, _map: Map.__subclasses__(), context: Context):
        # The map to control
        self.map = _map

        # The context
        self.context = context

        # display
        display = self.context.display
        display.unshift_layer("furniture_top", self.map.get_layer("furniture_top"))
        display.unshift_layer("furniture_bottom", self.map.get_layer("furniture_bottom"))
        display.unshift_layer("floor", self.map.get_layer("floor"))
        display.unshift_layer("ground", self.map.get_layer("ground"))

    def load(self, context: Context) -> None:
        """
        Loads the map.
        :param context: The game context.
        """
        self.map.load(context)


class HouseMap(Map):
    """
    House map.
    """

    def __init__(self):
        super().__init__(Size(60, 30))
        self._init()

    def _init(self):
        super()._init()
        furniture_top_layer: GridLayer = self.get_layer("furniture_top")
        house_renderer = HouseRenderer()
        house_renderer.render(furniture_top_layer, CoordinateSet.from_rect(Rect(10, 5, 20, 10)))

    def load(self, context: Context) -> None:
        pass


class FarmMap(Map):
    """
    Farm.
    """

    def __init__(self):
        super().__init__(Size(60, 30))
        self._init()

    def load(self, context: Context) -> None:
        display = context.game.display
        ground_layer: GridLayer = display.get_layer("ground")

        # Animation
        frames: List[Surface] = Frames.Water.list

        def update_water(index: int):
            for row in range(0, ground_layer.grid_size.height):
                for col in range(0, ground_layer.grid_size.width):
                    ground_layer.update_cell((col, row), frames[index])

        update_water(0)
        context.game.loop_manager.register(2, len(frames), update_water)
