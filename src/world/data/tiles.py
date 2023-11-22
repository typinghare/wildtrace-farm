"""
Tile resource module.
"""

from typing import Tuple
from pygame import Surface

from src.registry import RegistryUtil, Tag
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


class TileTags:
    """
    Tile tags.
    """

    COLLISION_OBJECT = Tag("COLLISION_OBJECT")
    ARABLE = Tag("ARABLE")


class Tiles:
    """
    Tile image resources.
    """

    # Grass square
    GrassSquare6 = register("grass_square/6", Tilesets.Grass, (0, 0))
    GrassSquare14 = register("grass_square/14", Tilesets.Grass, (16, 0))
    GrassSquare12 = register("grass_square/12", Tilesets.Grass, (32, 0))
    GrassSquare7 = register("grass_square/7", Tilesets.Grass, (0, 16))
    GrassSquare15 = register("grass_square/15", Tilesets.Grass, (16, 16))
    GrassSquare13 = register("grass_square/13", Tilesets.Grass, (32, 16))
    GrassSquare3 = register("grass_square/3", Tilesets.Grass, (0, 32))
    GrassSquare11 = register("grass_square/11", Tilesets.Grass, (16, 32))
    GrassSquare9 = register("grass_square/9", Tilesets.Grass, (32, 32))
    GrassSquare4 = register("grass_square/4", Tilesets.Grass, (48, 0))
    GrassSquare5 = register("grass_square/5", Tilesets.Grass, (48, 16))
    GrassSquare1 = register("grass_square/1", Tilesets.Grass, (48, 32))
    GrassSquare2 = register("grass_square/2", Tilesets.Grass, (0, 48))
    GrassSquare10 = register("grass_square/10", Tilesets.Grass, (16, 48))
    GrassSquare8 = register("grass_square/8", Tilesets.Grass, (32, 48))
    GrassSquare0 = register("grass_square/0", Tilesets.Grass, (48, 48))

    # Water
    Water0 = register("water/0", Tilesets.Water, (0, 0))
    Water1 = register("water/1", Tilesets.Water, (16, 0))
    Water2 = register("water/2", Tilesets.Water, (32, 0))
    Water3 = register("water/3", Tilesets.Water, (48, 0))

    # Furniture
    Picture0 = register("picture/0", Tilesets.Furniture, (0, 0))
    Picture1 = register("picture/1", Tilesets.Furniture, (16, 0))
    Picture2 = register("picture/2", Tilesets.Furniture, (32, 0))
    PottedPlant0 = register("potted_plant/0", Tilesets.Furniture, (48, 0))
    PottedPlant1 = register("potted_plant/1", Tilesets.Furniture, (64, 0))
    PottedPlant2 = register("potted_plant/2", Tilesets.Furniture, (80, 0))
    PottedMushroom0 = register("potted_mushroom/0", Tilesets.Furniture, (48, 0))
    PottedMushroom1 = register("potted_mushroom/1", Tilesets.Furniture, (64, 16))
    PottedMushroom2 = register("potted_mushroom/2", Tilesets.Furniture, (80, 16))
    BedUpGreen = register("bed/up/green", Tilesets.Furniture, (0, 16), (16, 32))
    BedUpCyan = register("bed/up/cyan", Tilesets.Furniture, (16, 16), (16, 32))
    BedUpMagenta = register("bed/up/magenta", Tilesets.Furniture, (32, 16), (16, 32))
    BedDownGreen = register("bed/down/green", Tilesets.Furniture, (0, 48), (16, 32))
    BedDownCyan = register("bed/down/cyan", Tilesets.Furniture, (16, 48), (16, 32))
    BedDownMagenta = register("bed/down/magenta", Tilesets.Furniture, (32, 48), (16, 32))
    Closet = register("closet", Tilesets.Furniture, (48, 32))
    ChairRight = register("chair/right", Tilesets.Furniture, (64, 32))
    ChairLeft = register("chair/left", Tilesets.Furniture, (80, 32))
    ChairDown = register("chair/left", Tilesets.Furniture, (96, 32))
    ChairUp = register("chair/left", Tilesets.Furniture, (112, 32))
    TableBig = register("table/big", Tilesets.Furniture, (48, 48))
    TableSmall = register("table/small", Tilesets.Furniture, (64, 48))
    Clock0 = register("clock/0", Tilesets.Furniture, (64, 48))
    Clock1 = register("clock/1", Tilesets.Furniture, (80, 48))
    Clock2 = register("clock/2", Tilesets.Furniture, (96, 48))
    CarpetSquareGreen = register("carpet/square/green", Tilesets.Furniture, (0, 80))
    CarpetSquareMagenta = register("carpet/square/magenta", Tilesets.Furniture, (16, 80))
    CarpetSquareCyan = register("carpet/square/cyan", Tilesets.Furniture, (32, 80))
    CarpetRectangleGreen = register(
        "carpet/rectangle/green", Tilesets.Furniture, (48, 80), (32, 16)
    )
    CarpetRectangleMagenta = register(
        "carpet/rectangle/magenta", Tilesets.Furniture, (80, 80), (32, 16)
    )
    CarpetRectangleCyan = register("carpet/rectangle/cyan", Tilesets.Furniture, (112, 80), (32, 16))

    # Wooden house
    WoodenHouse6 = register("wooden_house/6", Tilesets.WoodenHouse, (0, 16))
    WoodenHouse14 = register("wooden_house/13", Tilesets.WoodenHouse, (16, 16))
    WoodenHouse12 = register("wooden_house/12", Tilesets.WoodenHouse, (32, 16))
    WoodenHouse7 = register("wooden_house/7", Tilesets.WoodenHouse, (0, 32))
    WoodenHouse15 = register("wooden_house/15", Tilesets.WoodenHouse, (16, 32))
    WoodenHouse13 = register("wooden_house/13", Tilesets.WoodenHouse, (32, 32))
    WoodenHouse3 = register("wooden_house/3", Tilesets.WoodenHouse, (0, 48))
    WoodenHouse11 = register("wooden_house/11", Tilesets.WoodenHouse, (16, 48))
    WoodenHouse9 = register("wooden_house/9", Tilesets.WoodenHouse, (32, 48))

    # Wheat
    WheatSeed = register("wheat/seed", Tilesets.BasicPlants, (0, 0))
    WheatSeedling = register("wheat/seedling", Tilesets.BasicPlants, (16, 0))
    WheatVegetative = register("wheat/vegetative", Tilesets.BasicPlants, (32, 0))
    WheatBudding = register("wheat/budding", Tilesets.BasicPlants, (48, 0))
    WheatRipening = register("wheat/ripening", Tilesets.BasicPlants, (64, 0))
    WheatProduct = register("wheat/product", Tilesets.BasicPlants, (80, 0))

    # Beet
    BeetSeed = register("beet/seed", Tilesets.BasicPlants, (0, 16))
    BeetSeedling = register("beat/seedling", Tilesets.BasicPlants, (16, 16))
    BeetVegetative = register("beat/vegetative", Tilesets.BasicPlants, (32, 16))
    BeetBudding = register("beat/budding", Tilesets.BasicPlants, (48, 16))
    BeetRipening = register("beat/ripening", Tilesets.BasicPlants, (64, 16))
    BeetProduct = register("beat/product", Tilesets.BasicPlants, (80, 16))

    def __init__(self):
        # Collision object tag
        collision_objects = [Tiles.TableBig, Tiles.TableSmall]
        for collision_object in collision_objects:
            ref = Registries.Tile.get_ref(collision_object)
            ref.bind_tag(TileTags.COLLISION_OBJECT)
