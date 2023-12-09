"""
Tile set resource module.
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

    # Plants
    BasicPlants = register("tilesets/plants/basic_plants.png")
    Plants = register("tilesets/plants/plants.png")
    PlantsItem = register("tilesets/plants/plants_item.png")

    # Ground
    Grass = register("tilesets/ground/grass.png")
    Hills = register("tilesets/ground/grass_hill.png")
    TilledDirt = register("tilesets/ground/tilled_dirt.png")
    Water = register("tilesets/ground/water.png")
    Tree = register("tilesets/ground/tree.png")
    GroundDecoration = register("tilesets/ground/ground_decoration.png")

    # Building
    Furniture = register("tilesets/building/furniture.png")
    WoodenHouse = register("tilesets/building/wooden_house.png")
    Door = register("tilesets/building/door.png")
    Chest = register("tilesets/building/chest.png")
    Basket = register("tilesets/building/basket.png")
    WorkStation = register("tilesets/building/work_station.png")

    # Item
    ToolMaterial = register("tilesets/item/tool_material.png")

    # Character
    CharacterSpriteSheet = register("tilesets/character/sprite_sheet.png")
    Watering = register("tilesets/character/watering.png")
