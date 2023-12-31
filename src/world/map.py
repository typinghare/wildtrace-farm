"""
Map module
"""
from typing import Dict, List, Optional, Tuple, Any

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
        # The size (grid size) of the map
        self.size = size

        # The layers
        cell_size = settings.display_cell_size
        self.layers: Dict[str, GridLayer] = {
            "water": GridLayer(self.size, cell_size),
            "ground": GridLayer(self.size, cell_size),
            "floor": GridLayer(self.size, cell_size),
            "crop": GridLayer(self.size, cell_size),
            "furniture_bottom": GridLayer(self.size, cell_size),
            "furniture_top": GridLayer(self.size, cell_size),
        }

        # invisible block grid
        self.invisible_block_grid: None | Grid = None

    def get_layer(self, name: str) -> GridLayer:
        """
        Gets a layer.
        :param name: The name of the layer.
        """
        return self.layers[name]

    def all_layers(self) -> List[GridLayer]:
        """
        Returns all layers.
        """
        return list(self.layers.values())

    def clone(self) -> "Map":
        """
        Returns a deep copy of this map.
        """
        _map = Map(self.size)
        for name, layer in self.layers.items():
            _map.layers[name] = layer.clone()

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

    def __init__(self, _map: Map, context: Context):
        # The map to control
        self.map: Map | Any = _map

        # The context
        self.context: Context = context

        # Block grid; cells are booleans; a cell is marked as true if it is a collision object
        self.block_grid: Grid = Grid(self.map.size, False)

        # Offset for all layers
        self.offset: Vector2 = Vector2(0, 0)

    def set_layers_to_display(self) -> None:
        """
        Sets layers to the game display.
        """
        display = self.context.display
        for layer_name, layer in self.map.layers.items():
            display.set_layer(layer_name, layer)

    def load(self) -> None:
        """
        Loads the map.
        """
        self.map.load(self.context)

    def set_offset(self, offset: Vector2) -> None:
        """
        Sets the offset for all layers.
        """
        self.offset = offset
        for layer in self.map.all_layers():
            layer.offset = offset

    def set_rect(self, rect: Optional[Rect]) -> None:
        """
        Sets the rectangle for all layers.
        """
        for layer in self.map.all_layers():
            layer.rect = rect

    def refresh_block_grid(self) -> None:
        """
        Refreshes the block grid.
        """
        # Invisible block
        invisible_block_grid = self.map.invisible_block_grid
        if invisible_block_grid is not None:
            for index in range(len(invisible_block_grid)):
                if invisible_block_grid[index]:
                    self.block_grid[index] = True

        for layer in self.map.all_layers():
            self.refresh_block_grid_of_layer(layer)

    def refresh_block_grid_of_layer(self, layer):
        """
        Refreshes block grid of a certain layer.
        """
        size = self.map.size

        iterator = layer.grid.get_iterator((0, size.height), (0, size.width))
        for cell in iterator:
            surface = cell.surface
            index = self.block_grid.get_index(cell.coordinate)
            if self.block_grid[index] or surface is None:
                continue

            ref = Registries.Tile.get_ref_by_res(surface)
            if ref.contain_tag(TileTags.COLLISION_OBJECT):
                self.block_grid[index] = True

    def is_block(self, coordinate: Tuple[int, int]) -> bool:
        """
        Checks whether a coordinate is a blocked cell.
        """
        index = self.block_grid.get_index(coordinate)
        if index < 0 or index > len(self.block_grid):
            return False

        return self.block_grid[index]
