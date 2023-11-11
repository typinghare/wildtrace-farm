from typing import Tuple
from pygame import Surface

from src.registry import RegistryUtil
from src.core.settings import Settings
from .tile_sets import TileSets
from .registries import Registries
from ..util import crop_image, scale_image

scale_factor = Settings().display_scale_factor


def register(path: str, tile_set: Surface, pos: Tuple[int, int], size: Tuple[int, int]) -> Surface:
    """
    Registers a tile.
    :param path: The path of the tile resource.
    :param tile_set: The tile set to crop from.
    :param pos: The position of the tile in the given tile set.
    :param size: The size of the tile (width, height).
    :return: The magnified tile image.
    """
    image = scale_image(crop_image(tile_set, pos, size), scale_factor)

    return Registries.TileSet.register(RegistryUtil.createLoc(path), image)


class Tiles:
    """
    Tile resources.
    """

    WheatSeed = register("wheat/seed", TileSets.BasicPlants, (0, 0), (16, 16))
    WheatSeedling = register("wheat/seedling", TileSets.BasicPlants, (16, 0), (16, 16))
    WheatVegetative = register("wheat/vegetative", TileSets.BasicPlants, (32, 0), (16, 16))
    WheatBudding = register("wheat/budding", TileSets.BasicPlants, (48, 0), (16, 16))
    WheatRipening = register("wheat/ripening", TileSets.BasicPlants, (64, 0), (16, 16))
    WheatProduct = register("wheat/product", TileSets.BasicPlants, (80, 0), (16, 16))

    BeetSeed = register("beet/seed", TileSets.BasicPlants, (0, 16), (16, 16))
    BeetSeedling = register("beat/seedling", TileSets.BasicPlants, (16, 16), (16, 16))
    BeetVegetative = register("beat/vegetative", TileSets.BasicPlants, (32, 16), (16, 16))
    BeetBudding = register("beat/budding", TileSets.BasicPlants, (48, 16), (16, 16))
    BeetRipening = register("beat/ripening", TileSets.BasicPlants, (64, 16), (16, 16))
    BeetProduct = register("beat/product", TileSets.BasicPlants, (80, 16), (16, 16))
