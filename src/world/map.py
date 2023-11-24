"""
Map module
"""
from typing import Dict, List, Optional

from pygame import Vector2, Rect

from src.core.common import Size, Grid
from src.core.settings import Settings
from src.core.context import Context
from src.core.display import GridLayer
from src.world.data.registries import Registries
from src.world.data.tiles import TileTags

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

        # Block grid; cells are booleans; a cell is marked as true if it is a collision object
        self.block_grid: Grid = Grid(self.size, False)

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

    def all_layers(self) -> List[GridLayer]:
        """
        Returns all layers.
        """
        return list(self._layers.values())

    def refresh_block_grid(self) -> None:
        """
        Refreshes the block grid.
        """
        for layer in self._layers.values():
            self.refresh_block_grid_of_layer(layer)

    def refresh_block_grid_of_layer(self, layer):
        """
        Refreshes block grid of a certain layer.
        """
        iterator = layer.grid.get_iterator((0, self.size.height), (0, self.size.width))
        for cell in iterator:
            surface = cell.surface
            if surface is None:
                continue

            ref = Registries.Tile.get_ref_by_res(surface)
            if ref.contain_tag(TileTags.COLLISION_OBJECT):
                self.block_grid.set(cell.coordinate, True)

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
        self.map: Map = _map

        # The context
        self.context: Context = context

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

    def set_offset(self, offset: Vector2) -> None:
        """
        Sets the offset for all layers.
        """
        for layer in self.map.all_layers():
            layer.offset = offset

    def set_rect(self, rect: Optional[Rect]) -> None:
        """
        Sets the rectangle for all layers.
        """
        for layer in self.map.all_layers():
            layer.rect = rect
