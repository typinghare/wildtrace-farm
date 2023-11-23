"""
Farm map module.
"""

from typing import List

from pygame import Surface

from src.core.common import Size
from src.core.context import Context
from src.core.display import GridLayer
from src.world.data.frames import Frames
from src.world.map import Map


class FarmMap(Map):
    """
    Farm map.
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
