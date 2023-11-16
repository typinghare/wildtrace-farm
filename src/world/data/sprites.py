from typing import Tuple
from pygame import Surface

from src.registry import RegistryUtil
from src.core.settings import Settings
from src.world.data.registries import Registries
from src.world.data.tiles import Tilesets
from ..util import crop_image, scale_image

scale_factor: int = Settings().display_scale_factor


def register(
    path: str, tile_set: Surface, pos: Tuple[int, int], size: Tuple[int, int] = (48, 48)
) -> Surface:
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

    CharacterDownIdle0 = register("down/0", Tilesets.CharacterSpriteSheet, (48 * 0, 0))
    CharacterDownIdle1 = register("down/1", Tilesets.CharacterSpriteSheet, (48 * 1, 0))
    CharacterDownIdle2 = register("down/2", Tilesets.CharacterSpriteSheet, (48 * 2, 0))
    CharacterDownIdle3 = register("down/3", Tilesets.CharacterSpriteSheet, (48 * 3, 0))
    CharacterDownIdle4 = register("down/4", Tilesets.CharacterSpriteSheet, (48 * 4, 0))
    CharacterDownIdle5 = register("down/5", Tilesets.CharacterSpriteSheet, (48 * 5, 0))
    CharacterDownIdle6 = register("down/6", Tilesets.CharacterSpriteSheet, (48 * 6, 0))
    CharacterDownIdle7 = register("down/7", Tilesets.CharacterSpriteSheet, (48 * 7, 0))
