"""
House map module.
"""

from pygame import Rect

from src.core.common import Size, CoordinateSet, Grid
from src.core.display import GridLayer
from src.world.data.renderers import Renderers
from src.world.data.tiles import Tiles
from src.world.map import Map


class HomeMap(Map):
    """
    House map.
    """

    def __init__(self):
        super().__init__(Size(8, 6))

        self.floor: GridLayer = self.get_layer("floor")
        self.furniture_bottom: GridLayer = self.get_layer("furniture_bottom")
        self.furniture_top: GridLayer = self.get_layer("furniture_top")
        self.invisible_block_grid = Grid(self.size)

        self._init_wall()
        self._init_furniture()

    def _init_wall(self):
        wall_rect = CoordinateSet.from_rect(Rect(0, 0, self.size.width, self.size.height))
        Renderers.House.render(self.floor, wall_rect)

    def _init_furniture(self):
        # Bed
        self.furniture_bottom.update_cell((1, 3), Tiles.BedUpCyan)
        self.invisible_block_grid.set((1, 4), True)

        # Table and chairs
        self.furniture_bottom.update_cell((2, 1), Tiles.TableBig)
        self.furniture_bottom.update_cell((1, 1), Tiles.ChairRight)
        self.furniture_bottom.update_cell((3, 1), Tiles.ChairLeft)

        # Door
        self.furniture_bottom.update_cell((4, 5), Tiles.Door5)

        # Pictures on the wall
        self.furniture_bottom.update_cell((2, 0), Tiles.Picture0)
        self.furniture_bottom.update_cell((3, 0), Tiles.Picture1)

        # Clock on the wall
        self.furniture_bottom.update_cell((5, 0), Tiles.Clock2)

        # Chest
        self.furniture_bottom.update_cell((6, 1), Tiles.ChestFront0)
