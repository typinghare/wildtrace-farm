from typing import Tuple
from pygame import Surface

from src.registry import RegistryUtil
from src.core.settings import Settings
from .tilesets import Tilesets
from .registries import Registries
from ..util import crop_image, scale_image

scale_factor = Settings().display_scale_factor


def register(
    path: str, tile_set: Surface, pos: Tuple[int, int], size: Tuple[int, int] = (16, 16)
) -> Surface:
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

    # Grass square
    GrassSquare0 = register("grass-square/0", Tilesets.Grass, (16, 48))
    GrassSquare1 = register("grass-square/1", Tilesets.Grass, (32, 48))
    GrassSquare2 = register("grass-square/2", Tilesets.Grass, (48, 48))
    GrassSquare3 = register("grass-square/3", Tilesets.Grass, (16, 64))
    GrassSquare4 = register("grass-square/4", Tilesets.Grass, (32, 64))
    GrassSquare5 = register("grass-square/5", Tilesets.Grass, (48, 64))
    GrassSquare6 = register("grass-square/6", Tilesets.Grass, (16, 80))
    GrassSquare7 = register("grass-square/7", Tilesets.Grass, (32, 80))
    GrassSquare8 = register("grass-square/8", Tilesets.Grass, (48, 80))

    # Water
    Water0 = register("water/0", Tilesets.Water, (0, 0))
    Water1 = register("water/1", Tilesets.Water, (16, 0))
    Water2 = register("water/2", Tilesets.Water, (32, 0))
    Water3 = register("water/3", Tilesets.Water, (48, 0))

    WheatSeed = register("wheat/seed", Tilesets.BasicPlants, (0, 0))
    WheatSeedling = register("wheat/seedling", Tilesets.BasicPlants, (16, 0))
    WheatVegetative = register("wheat/vegetative", Tilesets.BasicPlants, (32, 0))
    WheatBudding = register("wheat/budding", Tilesets.BasicPlants, (48, 0))
    WheatRipening = register("wheat/ripening", Tilesets.BasicPlants, (64, 0))
    WheatProduct = register("wheat/product", Tilesets.BasicPlants, (80, 0))

    BeetSeed = register("beet/seed", Tilesets.BasicPlants, (0, 16))
    BeetSeedling = register("beat/seedling", Tilesets.BasicPlants, (16, 16))
    BeetVegetative = register("beat/vegetative", Tilesets.BasicPlants, (32, 16))
    BeetBudding = register("beat/budding", Tilesets.BasicPlants, (48, 16))
    BeetRipening = register("beat/ripening", Tilesets.BasicPlants, (64, 16))
    BeetProduct = register("beat/product", Tilesets.BasicPlants, (80, 16))
