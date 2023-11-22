"""
Renderer module.
"""
from typing import Tuple

from abc import ABC, abstractmethod

from src.core.common import CoordinateSet, Grid
from src.core.display import GridLayer
from src.world.data.tiles import Tiles


class Renderer(ABC):
    """
    Renderers can render an area.
    """

    @abstractmethod
    def render(self, grid_layer: GridLayer, coordinate_set: CoordinateSet) -> None:
        """
        Renders a specified area of a layer.
        :param grid_layer: The grid layer to render.
        :param coordinate_set: The coordinates of the cells to render.
        """

    @staticmethod
    def get_status(coordinate: Tuple[int, int], coordinate_set: CoordinateSet) -> int:
        """
        Calculates the status of a specified coordinate.
        :param coordinate: The coordinate to check.
        :param coordinate_set: The coordinate set to test.
        :return An integer ranges from 0 to 15.
        """
        up = (coordinate[0], coordinate[1] - 1)
        left = (coordinate[0] - 1, coordinate[1])
        down = (coordinate[0], coordinate[1] + 1)
        right = (coordinate[0] + 1, coordinate[1])

        status = 0
        if coordinate_set.has(up):
            status += 0b0001
        if coordinate_set.has(right):
            status += 0b0010
        if coordinate_set.has(down):
            status += 0b0100
        if coordinate_set.has(left):
            status += 0b1000

        # Status Map
        # 0b0000(00): []
        # 0b0001(01): [up]
        # 0b0010(02): [right]
        # 0b0011(03): [up, right]
        # 0b0100(04): [down]
        # 0b0101(05): [up, down]
        # 0b0110(06): [right, down]
        # 0b0111(07): [up, right, down]
        # 0b1000(08): [left]
        # 0b1001(09): [up, left]
        # 0b1010(10): [right, left]
        # 0b1011(11): [up, right, left]
        # 0b1100(12): [down, left]
        # 0b1101(13): [up, down, left]
        # 0b1110(14): [right, down, left]
        # 0b1111(15): [up, right, down, left]

        return status


class HouseRenderer(Renderer):
    """
    House renderer.
    """

    def __init__(self):
        self._tiles = [
            Tiles.WoodenHouse15,
            Tiles.WoodenHouse15,
            Tiles.WoodenHouse15,
            Tiles.WoodenHouse3,
            Tiles.WoodenHouse15,
            Tiles.WoodenHouse15,
            Tiles.WoodenHouse6,
            Tiles.WoodenHouse7,
            Tiles.WoodenHouse15,
            Tiles.WoodenHouse9,
            Tiles.WoodenHouse15,
            Tiles.WoodenHouse11,
            Tiles.WoodenHouse12,
            Tiles.WoodenHouse13,
            Tiles.WoodenHouse14,
            Tiles.WoodenHouse15,
        ]

    def render(self, grid_layer: GridLayer, coordinate_set: CoordinateSet) -> None:
        for coordinate in coordinate_set.all():
            status = self.get_status(coordinate, coordinate_set)
            grid_layer.update_cell(coordinate, self._tiles[status])


class GrassRenderer(Renderer):
    """
    Grass renderer.
    """

    def __init__(self):
        self._tiles = [
            Tiles.GrassSquare0,
            Tiles.GrassSquare1,
            Tiles.GrassSquare2,
            Tiles.GrassSquare3,
            Tiles.GrassSquare4,
            Tiles.GrassSquare5,
            Tiles.GrassSquare6,
            Tiles.GrassSquare7,
            Tiles.GrassSquare9,
            Tiles.GrassSquare10,
            Tiles.GrassSquare11,
            Tiles.GrassSquare12,
            Tiles.GrassSquare13,
            Tiles.GrassSquare14,
            Tiles.GrassSquare15,
        ]

    def render(self, grid_layer: GridLayer, coordinate_set: CoordinateSet) -> None:
        for coordinate in coordinate_set.all():
            status = self.get_status(coordinate, coordinate_set)
            grid_layer.update_cell(coordinate, self._tiles[status])
