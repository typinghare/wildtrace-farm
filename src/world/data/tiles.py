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

default_scale_factor = Settings().display_tile_scale_factor


def register(
    path: str,
    tile_set: Surface,
    pos: Tuple[int, int],
    size: Tuple[int, int] = (16, 16),
    scale_factor: int = default_scale_factor,
) -> Surface:
    """
    Registers a tile.
    :param path: The path of the tile resource.
    :param tile_set: The tile set to crop from.
    :param pos: The position of the tile in the given tile set.
    :param size: The size of the tile (width, height).
    :param scale_factor: The scale factor.
    :return: The magnified tile image.
    """
    image = scale_image(crop_image(tile_set, pos, size), scale_factor)

    return Registries.Tile.register(RegistryUtil.createLoc(path), image)


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

    # Grass
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

    # Tilled dirt
    TilledDirt6 = register("tilled_dirt/0", Tilesets.TilledDirt, (16, 48))
    TilledDirt14 = register("tilled_dirt/0", Tilesets.TilledDirt, (32, 48))
    TilledDirt12 = register("tilled_dirt/0", Tilesets.TilledDirt, (48, 48))
    TilledDirt7 = register("tilled_dirt/0", Tilesets.TilledDirt, (16, 64))
    TilledDirt15 = register("tilled_dirt/0", Tilesets.TilledDirt, (32, 64))
    TilledDirt13 = register("tilled_dirt/0", Tilesets.TilledDirt, (48, 64))
    TilledDirt3 = register("tilled_dirt/0", Tilesets.TilledDirt, (16, 80))
    TilledDirt11 = register("tilled_dirt/0", Tilesets.TilledDirt, (32, 80))
    TilledDirt9 = register("tilled_dirt/0", Tilesets.TilledDirt, (48, 80))
    TilledDirt4 = register("tilled_dirt/0", Tilesets.TilledDirt, (0, 48))
    TilledDirt5 = register("tilled_dirt/0", Tilesets.TilledDirt, (0, 64))
    TilledDirt1 = register("tilled_dirt/0", Tilesets.TilledDirt, (0, 80))
    TilledDirt2 = register("tilled_dirt/0", Tilesets.TilledDirt, (16, 96))
    TilledDirt10 = register("tilled_dirt/0", Tilesets.TilledDirt, (32, 96))
    TilledDirt8 = register("tilled_dirt/0", Tilesets.TilledDirt, (48, 96))
    TilledDirt0 = register("tilled_dirt/0", Tilesets.TilledDirt, (0, 96))

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
    Clock0 = register("clock/0", Tilesets.Furniture, (80, 48))
    Clock1 = register("clock/1", Tilesets.Furniture, (96, 48))
    Clock2 = register("clock/2", Tilesets.Furniture, (112, 48))
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
    Roof0 = register("roof/0", Tilesets.WoodenHouse, (48, 0))
    Roof1 = register("roof/1", Tilesets.WoodenHouse, (64, 0))
    Roof2 = register("roof/2", Tilesets.WoodenHouse, (80, 0))
    Roof3 = register("roof/3", Tilesets.WoodenHouse, (48, 16))
    Roof4 = register("roof/4", Tilesets.WoodenHouse, (64, 16))
    Roof5 = register("roof/5", Tilesets.WoodenHouse, (80, 16))
    Roof6 = register("roof/6", Tilesets.WoodenHouse, (48, 32))
    Roof7 = register("roof/7", Tilesets.WoodenHouse, (64, 32))
    Roof8 = register("roof/8", Tilesets.WoodenHouse, (80, 32))
    Roof9 = register("roof/9", Tilesets.WoodenHouse, (48, 48))
    Roof10 = register("roof/10", Tilesets.WoodenHouse, (64, 48))
    Roof11 = register("roof/11", Tilesets.WoodenHouse, (80, 48))
    Roof12 = register("roof/12", Tilesets.WoodenHouse, (48, 64))
    Roof13 = register("roof/13", Tilesets.WoodenHouse, (64, 64))
    Roof14 = register("roof/14", Tilesets.WoodenHouse, (80, 64))

    # Doors
    Door0 = register("door/0", Tilesets.Door, (0, 0))
    Door1 = register("door/1", Tilesets.Door, (16, 0))
    Door2 = register("door/2", Tilesets.Door, (32, 0))
    Door3 = register("door/3", Tilesets.Door, (48, 0))
    Door4 = register("door/4", Tilesets.Door, (64, 0))
    Door5 = register("door/5", Tilesets.Door, (80, 0))

    # Chest
    ChestFront0 = register("chest/front/0", Tilesets.Chest, (16, 16), (16, 16), 3)
    ChestFront1 = register("chest/front/1", Tilesets.Chest, (80, 16), (16, 16), 3)
    ChestFront2 = register("chest/front/2", Tilesets.Chest, (128, 16), (16, 16), 3)
    ChestFront3 = register("chest/front/3", Tilesets.Chest, (176, 16), (16, 16), 3)
    ChestFront4 = register("chest/front/4", Tilesets.Chest, (224, 16), (16, 16), 3)

    # Tools
    ToolWaterCan = register("tool/water_can", Tilesets.ToolMaterial, (0, 0))
    ToolHoe = register("tool/hoe", Tilesets.ToolMaterial, (32, 0))

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


# Collision object tag
collision_objects = [
    Tiles.WoodenHouse6,
    Tiles.WoodenHouse14,
    Tiles.WoodenHouse12,
    Tiles.WoodenHouse7,
    Tiles.WoodenHouse13,
    Tiles.WoodenHouse3,
    Tiles.WoodenHouse11,
    Tiles.WoodenHouse9,
    Tiles.Door0,
    Tiles.Door1,
    Tiles.Door2,
    Tiles.Door3,
    Tiles.Door4,
    Tiles.Door5,
    Tiles.TableBig,
    Tiles.TableSmall,
    Tiles.ChairUp,
    Tiles.ChairRight,
    Tiles.ChairDown,
    Tiles.ChairLeft,
    Tiles.ChestFront0,
    Tiles.ChestFront1,
    Tiles.ChestFront2,
    Tiles.ChestFront3,
    Tiles.ChestFront4,
]

for collision_object in collision_objects:
    ref = Registries.Tile.get_ref_by_res(collision_object)
    ref.bind_tag(TileTags.COLLISION_OBJECT)
