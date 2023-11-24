"""
House map module.
"""

from pygame import Rect

from src.core.common import Size, CoordinateSet
from src.core.context import Context
from src.core.display import GridLayer
from src.world.map import Map
from src.world.renderer import HouseRenderer


class HomeMap(Map):
    """
    House map.
    """

    def __init__(self):
        super().__init__(Size(10, 8))
        self._init()

    def _init(self):
        super()._init()
        furniture_top_layer: GridLayer = self.get_layer("furniture_top")
        house_renderer = HouseRenderer()
        wall_rect = CoordinateSet.from_rect(Rect(0, 0, self.size.width, self.size.height))
        house_renderer.render(furniture_top_layer, wall_rect)

    def load(self, context: Context) -> None:
        pass
