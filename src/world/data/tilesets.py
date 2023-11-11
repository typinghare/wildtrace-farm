"""
Tile set resources.
"""

import os
import pygame
from pygame import Surface

from src.registry import RegistryUtil
from src.core.settings import Settings
from .registries import Registries


settings = Settings()


def register(path: str) -> Surface:
    """
    Registers a tile set.
    :param path: The path of the tile set file.
    :return: The loaded image.
    """
    abs_path = os.path.join(settings.assets_dir, path)

    return Registries.TileSet.register(RegistryUtil.createLoc(path), pygame.image.load(abs_path))


class Tilesets:
    """
    Tileset resources. These are the original images.
    """

    BasicPlants = register("tilesets/plants/basic_plants.png")
    FarmingPlants = register("tilesets/plants/farming_plants.png")
    Grass = register("tilesets/ground/grass.png")
    Hills = register("tilesets/ground/hills.png")
    TilledDirt = register("tilesets/ground/tilled_dirt.png")
    Water = register("tilesets/ground/water.png")
