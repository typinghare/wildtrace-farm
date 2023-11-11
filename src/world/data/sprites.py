from typing import Tuple
from pygame import Surface

from src.registry import RegistryUtil
from src.core.settings import Settings
from .tilesets import Tilesets
from .registries import Registries
from ..util import crop_image, scale_image

scale_factor = Settings().display_scale_factor


def register(path: str, tile_set: Surface, pos: Tuple[int, int], size: Tuple[int, int]) -> Surface:
    """
    Registers a sprite.
    :param path: The path of the sprite resource.
    :param tile_set: The tile set to crop from.
    :param pos: The position of the tile in the given tile set.
    :param size: The size of the tile (width, height).
    :return: The magnified sprite image.
    """
    image = scale_image(crop_image(tile_set, pos, size), scale_factor)

    return Registries.TileSet.register(RegistryUtil.createLoc(path), image)


class Sprites:
    """
    Sprite resources.
    """
