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

    CharacterIdleUp0 = register("character/idle/up/0", Tilesets.CharacterSpriteSheet, (48 * 0, 48))
    CharacterIdleUp1 = register("character/idle/up/1", Tilesets.CharacterSpriteSheet, (48 * 1, 48))
    CharacterIdleUp2 = register("character/idle/up/2", Tilesets.CharacterSpriteSheet, (48 * 2, 48))
    CharacterIdleUp3 = register("character/idle/up/3", Tilesets.CharacterSpriteSheet, (48 * 3, 48))
    CharacterIdleUp4 = register("character/idle/up/4", Tilesets.CharacterSpriteSheet, (48 * 4, 48))
    CharacterIdleUp5 = register("character/idle/up/5", Tilesets.CharacterSpriteSheet, (48 * 5, 48))
    CharacterIdleUp6 = register("character/idle/up/6", Tilesets.CharacterSpriteSheet, (48 * 6, 48))
    CharacterIdleUp7 = register("character/idle/up/7", Tilesets.CharacterSpriteSheet, (48 * 7, 48))

    CharacterIdleRight0 = register(
        "character/idle/right/0", Tilesets.CharacterSpriteSheet, (48 * 0, 48 * 3)
    )
    CharacterIdleRight1 = register(
        "character/idle/right/1", Tilesets.CharacterSpriteSheet, (48 * 1, 48 * 3)
    )
    CharacterIdleRight2 = register(
        "character/idle/right/2", Tilesets.CharacterSpriteSheet, (48 * 2, 48 * 3)
    )
    CharacterIdleRight3 = register(
        "character/idle/right/3", Tilesets.CharacterSpriteSheet, (48 * 3, 48 * 3)
    )
    CharacterIdleRight4 = register(
        "character/idle/right/4", Tilesets.CharacterSpriteSheet, (48 * 4, 48 * 3)
    )
    CharacterIdleRight5 = register(
        "character/idle/right/5", Tilesets.CharacterSpriteSheet, (48 * 5, 48 * 3)
    )
    CharacterIdleRight6 = register(
        "character/idle/right/6", Tilesets.CharacterSpriteSheet, (48 * 6, 48 * 3)
    )
    CharacterIdleRight7 = register(
        "character/idle/right/7", Tilesets.CharacterSpriteSheet, (48 * 7, 48 * 3)
    )

    CharacterIdleDown0 = register(
        "character/idle/down/0", Tilesets.CharacterSpriteSheet, (48 * 0, 0)
    )
    CharacterIdleDown1 = register(
        "character/idle/down/1", Tilesets.CharacterSpriteSheet, (48 * 1, 0)
    )
    CharacterIdleDown2 = register(
        "character/idle/down/2", Tilesets.CharacterSpriteSheet, (48 * 2, 0)
    )
    CharacterIdleDown3 = register(
        "character/idle/down/3", Tilesets.CharacterSpriteSheet, (48 * 3, 0)
    )
    CharacterIdleDown4 = register(
        "character/idle/down/4", Tilesets.CharacterSpriteSheet, (48 * 4, 0)
    )
    CharacterIdleDown5 = register(
        "character/idle/down/5", Tilesets.CharacterSpriteSheet, (48 * 5, 0)
    )
    CharacterIdleDown6 = register(
        "character/idle/down/6", Tilesets.CharacterSpriteSheet, (48 * 6, 0)
    )
    CharacterIdleDown7 = register(
        "character/idle/down/7", Tilesets.CharacterSpriteSheet, (48 * 7, 0)
    )

    CharacterIdleLeft0 = register(
        "character/idle/left/0", Tilesets.CharacterSpriteSheet, (48 * 0, 48 * 2)
    )
    CharacterIdleLeft1 = register(
        "character/idle/left/1", Tilesets.CharacterSpriteSheet, (48 * 1, 48 * 2)
    )
    CharacterIdleLeft2 = register(
        "character/idle/left/2", Tilesets.CharacterSpriteSheet, (48 * 2, 48 * 2)
    )
    CharacterIdleLeft3 = register(
        "character/idle/left/3", Tilesets.CharacterSpriteSheet, (48 * 3, 48 * 2)
    )
    CharacterIdleLeft4 = register(
        "character/idle/left/4", Tilesets.CharacterSpriteSheet, (48 * 4, 48 * 2)
    )
    CharacterIdleLeft5 = register(
        "character/idle/left/5", Tilesets.CharacterSpriteSheet, (48 * 5, 48 * 2)
    )
    CharacterIdleLeft6 = register(
        "character/idle/left/6", Tilesets.CharacterSpriteSheet, (48 * 6, 48 * 2)
    )
    CharacterIdleLeft7 = register(
        "character/idle/left/7", Tilesets.CharacterSpriteSheet, (48 * 7, 48 * 2)
    )

    CharacterMoveUp0 = register(
        "character/move/up/0", Tilesets.CharacterSpriteSheet, (48 * 0, 48 * 5)
    )
    CharacterMoveUp1 = register(
        "character/move/up/1", Tilesets.CharacterSpriteSheet, (48 * 1, 48 * 5)
    )
    CharacterMoveUp2 = register(
        "character/move/up/2", Tilesets.CharacterSpriteSheet, (48 * 2, 48 * 5)
    )
    CharacterMoveUp3 = register(
        "character/move/up/3", Tilesets.CharacterSpriteSheet, (48 * 3, 48 * 5)
    )
    CharacterMoveUp4 = register(
        "character/move/up/4", Tilesets.CharacterSpriteSheet, (48 * 4, 48 * 5)
    )
    CharacterMoveUp5 = register(
        "character/move/up/5", Tilesets.CharacterSpriteSheet, (48 * 5, 48 * 5)
    )
    CharacterMoveUp6 = register(
        "character/move/up/6", Tilesets.CharacterSpriteSheet, (48 * 6, 48 * 5)
    )
    CharacterMoveUp7 = register(
        "character/move/up/7", Tilesets.CharacterSpriteSheet, (48 * 7, 48 * 5)
    )

    CharacterMoveRight0 = register(
        "character/move/right/0", Tilesets.CharacterSpriteSheet, (48 * 0, 48 * 6)
    )
    CharacterMoveRight1 = register(
        "character/move/right/1", Tilesets.CharacterSpriteSheet, (48 * 1, 48 * 6)
    )
    CharacterMoveRight2 = register(
        "character/move/right/2", Tilesets.CharacterSpriteSheet, (48 * 2, 48 * 6)
    )
    CharacterMoveRight3 = register(
        "character/move/right/3", Tilesets.CharacterSpriteSheet, (48 * 3, 48 * 6)
    )
    CharacterMoveRight4 = register(
        "character/move/right/4", Tilesets.CharacterSpriteSheet, (48 * 4, 48 * 6)
    )
    CharacterMoveRight5 = register(
        "character/move/right/5", Tilesets.CharacterSpriteSheet, (48 * 5, 48 * 6)
    )
    CharacterMoveRight6 = register(
        "character/move/right/6", Tilesets.CharacterSpriteSheet, (48 * 6, 48 * 6)
    )
    CharacterMoveRight7 = register(
        "character/move/right/7", Tilesets.CharacterSpriteSheet, (48 * 7, 48 * 6)
    )

    CharacterMoveDown0 = register(
        "character/move/down/0", Tilesets.CharacterSpriteSheet, (48 * 0, 48 * 4)
    )
    CharacterMoveDown1 = register(
        "character/move/down/1", Tilesets.CharacterSpriteSheet, (48 * 1, 48 * 4)
    )
    CharacterMoveDown2 = register(
        "character/move/down/2", Tilesets.CharacterSpriteSheet, (48 * 2, 48 * 4)
    )
    CharacterMoveDown3 = register(
        "character/move/down/3", Tilesets.CharacterSpriteSheet, (48 * 3, 48 * 4)
    )
    CharacterMoveDown4 = register(
        "character/move/down/4", Tilesets.CharacterSpriteSheet, (48 * 4, 48 * 4)
    )
    CharacterMoveDown5 = register(
        "character/move/down/5", Tilesets.CharacterSpriteSheet, (48 * 5, 48 * 4)
    )
    CharacterMoveDown6 = register(
        "character/move/down/6", Tilesets.CharacterSpriteSheet, (48 * 6, 48 * 4)
    )
    CharacterMoveDown7 = register(
        "character/move/down/7", Tilesets.CharacterSpriteSheet, (48 * 7, 48 * 4)
    )

    CharacterMoveLeft0 = register(
        "character/move/left/0", Tilesets.CharacterSpriteSheet, (48 * 0, 48 * 7)
    )
    CharacterMoveLeft1 = register(
        "character/move/left/1", Tilesets.CharacterSpriteSheet, (48 * 1, 48 * 7)
    )
    CharacterMoveLeft2 = register(
        "character/move/left/2", Tilesets.CharacterSpriteSheet, (48 * 2, 48 * 7)
    )
    CharacterMoveLeft3 = register(
        "character/move/left/3", Tilesets.CharacterSpriteSheet, (48 * 3, 48 * 7)
    )
    CharacterMoveLeft4 = register(
        "character/move/left/4", Tilesets.CharacterSpriteSheet, (48 * 4, 48 * 7)
    )
    CharacterMoveLeft5 = register(
        "character/move/left/5", Tilesets.CharacterSpriteSheet, (48 * 5, 48 * 7)
    )
    CharacterMoveLeft6 = register(
        "character/move/left/6", Tilesets.CharacterSpriteSheet, (48 * 6, 48 * 7)
    )
    CharacterMoveLeft7 = register(
        "character/move/left/7", Tilesets.CharacterSpriteSheet, (48 * 7, 48 * 7)
    )
