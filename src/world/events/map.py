"""
Map crafting events.
"""
from typing import List

from pygame import Surface, Rect

from src.core.common import CoordinateSet
from src.core.context import Context
from src.core.display import GridLayer
from src.world.data.frames import Frames
from src.world.renderer import HouseRenderer


def init_water(context: Context) -> None:
    """
    Initializes water.
    """
