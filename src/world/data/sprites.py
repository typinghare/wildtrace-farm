"""
Sprite resource module.
"""

from typing import Tuple
from pygame import Surface

from src.registry import RegistryUtil
from src.core.settings import Settings
from src.world.data.registries import Registries
from src.world.data.tiles import Tilesets
from ..util import crop_image, scale_image

tile_sf: int = Settings().display_tile_sf
character_sf: int = Settings().display_character_sf


def register(
    path: str,
    tile_set: Surface,
    pos: Tuple[int, int],
    size: Tuple[int, int] = (48, 48),
    is_character: bool = False,
) -> Surface:
    """
    Registers a sprite image.
    :param path: The path of the sprite resource.
    :param tile_set: The tile set to crop from.
    :param pos: The position of the tile in the given tile set.
    :param size: The size of the tile (width, height).
    :param is_character: Whether the sprite is the character.
    :return: The magnified sprite image.
    """
    sf = character_sf if is_character else tile_sf
    image = scale_image(crop_image(tile_set, pos, size), sf)

    return Registries.TileSet.register(RegistryUtil.createLoc(path), image)


class Sprites:
    """
    Sprite image resources.
    """

    CharacterIdleUp0 = register(
        "character/idle/up/0", Tilesets.CharacterSpriteSheet, (48 * 0, 48), is_character=True
    )
    CharacterIdleUp1 = register(
        "character/idle/up/1", Tilesets.CharacterSpriteSheet, (48 * 1, 48), is_character=True
    )
    CharacterIdleUp2 = register(
        "character/idle/up/2", Tilesets.CharacterSpriteSheet, (48 * 2, 48), is_character=True
    )
    CharacterIdleUp3 = register(
        "character/idle/up/3", Tilesets.CharacterSpriteSheet, (48 * 3, 48), is_character=True
    )
    CharacterIdleUp4 = register(
        "character/idle/up/4", Tilesets.CharacterSpriteSheet, (48 * 4, 48), is_character=True
    )
    CharacterIdleUp5 = register(
        "character/idle/up/5", Tilesets.CharacterSpriteSheet, (48 * 5, 48), is_character=True
    )
    CharacterIdleUp6 = register(
        "character/idle/up/6", Tilesets.CharacterSpriteSheet, (48 * 6, 48), is_character=True
    )
    CharacterIdleUp7 = register(
        "character/idle/up/7", Tilesets.CharacterSpriteSheet, (48 * 7, 48), is_character=True
    )

    CharacterIdleRight0 = register(
        "character/idle/right/0", Tilesets.CharacterSpriteSheet, (48 * 0, 48 * 3), is_character=True
    )
    CharacterIdleRight1 = register(
        "character/idle/right/1", Tilesets.CharacterSpriteSheet, (48 * 1, 48 * 3), is_character=True
    )
    CharacterIdleRight2 = register(
        "character/idle/right/2", Tilesets.CharacterSpriteSheet, (48 * 2, 48 * 3), is_character=True
    )
    CharacterIdleRight3 = register(
        "character/idle/right/3", Tilesets.CharacterSpriteSheet, (48 * 3, 48 * 3), is_character=True
    )
    CharacterIdleRight4 = register(
        "character/idle/right/4", Tilesets.CharacterSpriteSheet, (48 * 4, 48 * 3), is_character=True
    )
    CharacterIdleRight5 = register(
        "character/idle/right/5", Tilesets.CharacterSpriteSheet, (48 * 5, 48 * 3), is_character=True
    )
    CharacterIdleRight6 = register(
        "character/idle/right/6", Tilesets.CharacterSpriteSheet, (48 * 6, 48 * 3), is_character=True
    )
    CharacterIdleRight7 = register(
        "character/idle/right/7", Tilesets.CharacterSpriteSheet, (48 * 7, 48 * 3), is_character=True
    )

    CharacterIdleDown0 = register(
        "character/idle/down/0", Tilesets.CharacterSpriteSheet, (48 * 0, 0), is_character=True
    )
    CharacterIdleDown1 = register(
        "character/idle/down/1", Tilesets.CharacterSpriteSheet, (48 * 1, 0), is_character=True
    )
    CharacterIdleDown2 = register(
        "character/idle/down/2", Tilesets.CharacterSpriteSheet, (48 * 2, 0), is_character=True
    )
    CharacterIdleDown3 = register(
        "character/idle/down/3", Tilesets.CharacterSpriteSheet, (48 * 3, 0), is_character=True
    )
    CharacterIdleDown4 = register(
        "character/idle/down/4", Tilesets.CharacterSpriteSheet, (48 * 4, 0), is_character=True
    )
    CharacterIdleDown5 = register(
        "character/idle/down/5", Tilesets.CharacterSpriteSheet, (48 * 5, 0), is_character=True
    )
    CharacterIdleDown6 = register(
        "character/idle/down/6", Tilesets.CharacterSpriteSheet, (48 * 6, 0), is_character=True
    )
    CharacterIdleDown7 = register(
        "character/idle/down/7", Tilesets.CharacterSpriteSheet, (48 * 7, 0), is_character=True
    )

    CharacterIdleLeft0 = register(
        "character/idle/left/0", Tilesets.CharacterSpriteSheet, (48 * 0, 48 * 2), is_character=True
    )
    CharacterIdleLeft1 = register(
        "character/idle/left/1", Tilesets.CharacterSpriteSheet, (48 * 1, 48 * 2), is_character=True
    )
    CharacterIdleLeft2 = register(
        "character/idle/left/2", Tilesets.CharacterSpriteSheet, (48 * 2, 48 * 2), is_character=True
    )
    CharacterIdleLeft3 = register(
        "character/idle/left/3", Tilesets.CharacterSpriteSheet, (48 * 3, 48 * 2), is_character=True
    )
    CharacterIdleLeft4 = register(
        "character/idle/left/4", Tilesets.CharacterSpriteSheet, (48 * 4, 48 * 2), is_character=True
    )
    CharacterIdleLeft5 = register(
        "character/idle/left/5", Tilesets.CharacterSpriteSheet, (48 * 5, 48 * 2), is_character=True
    )
    CharacterIdleLeft6 = register(
        "character/idle/left/6", Tilesets.CharacterSpriteSheet, (48 * 6, 48 * 2), is_character=True
    )
    CharacterIdleLeft7 = register(
        "character/idle/left/7", Tilesets.CharacterSpriteSheet, (48 * 7, 48 * 2), is_character=True
    )

    CharacterMoveUp0 = register(
        "character/move/up/0", Tilesets.CharacterSpriteSheet, (48 * 0, 48 * 5), is_character=True
    )
    CharacterMoveUp1 = register(
        "character/move/up/1", Tilesets.CharacterSpriteSheet, (48 * 1, 48 * 5), is_character=True
    )
    CharacterMoveUp2 = register(
        "character/move/up/2", Tilesets.CharacterSpriteSheet, (48 * 2, 48 * 5), is_character=True
    )
    CharacterMoveUp3 = register(
        "character/move/up/3", Tilesets.CharacterSpriteSheet, (48 * 3, 48 * 5), is_character=True
    )
    CharacterMoveUp4 = register(
        "character/move/up/4", Tilesets.CharacterSpriteSheet, (48 * 4, 48 * 5), is_character=True
    )
    CharacterMoveUp5 = register(
        "character/move/up/5", Tilesets.CharacterSpriteSheet, (48 * 5, 48 * 5), is_character=True
    )
    CharacterMoveUp6 = register(
        "character/move/up/6", Tilesets.CharacterSpriteSheet, (48 * 6, 48 * 5), is_character=True
    )
    CharacterMoveUp7 = register(
        "character/move/up/7", Tilesets.CharacterSpriteSheet, (48 * 7, 48 * 5), is_character=True
    )

    CharacterMoveRight0 = register(
        "character/move/right/0", Tilesets.CharacterSpriteSheet, (48 * 0, 48 * 6), is_character=True
    )
    CharacterMoveRight1 = register(
        "character/move/right/1", Tilesets.CharacterSpriteSheet, (48 * 1, 48 * 6), is_character=True
    )
    CharacterMoveRight2 = register(
        "character/move/right/2", Tilesets.CharacterSpriteSheet, (48 * 2, 48 * 6), is_character=True
    )
    CharacterMoveRight3 = register(
        "character/move/right/3", Tilesets.CharacterSpriteSheet, (48 * 3, 48 * 6), is_character=True
    )
    CharacterMoveRight4 = register(
        "character/move/right/4", Tilesets.CharacterSpriteSheet, (48 * 4, 48 * 6), is_character=True
    )
    CharacterMoveRight5 = register(
        "character/move/right/5", Tilesets.CharacterSpriteSheet, (48 * 5, 48 * 6), is_character=True
    )
    CharacterMoveRight6 = register(
        "character/move/right/6", Tilesets.CharacterSpriteSheet, (48 * 6, 48 * 6), is_character=True
    )
    CharacterMoveRight7 = register(
        "character/move/right/7", Tilesets.CharacterSpriteSheet, (48 * 7, 48 * 6), is_character=True
    )

    CharacterMoveDown0 = register(
        "character/move/down/0", Tilesets.CharacterSpriteSheet, (48 * 0, 48 * 4), is_character=True
    )
    CharacterMoveDown1 = register(
        "character/move/down/1", Tilesets.CharacterSpriteSheet, (48 * 1, 48 * 4), is_character=True
    )
    CharacterMoveDown2 = register(
        "character/move/down/2", Tilesets.CharacterSpriteSheet, (48 * 2, 48 * 4), is_character=True
    )
    CharacterMoveDown3 = register(
        "character/move/down/3", Tilesets.CharacterSpriteSheet, (48 * 3, 48 * 4), is_character=True
    )
    CharacterMoveDown4 = register(
        "character/move/down/4", Tilesets.CharacterSpriteSheet, (48 * 4, 48 * 4), is_character=True
    )
    CharacterMoveDown5 = register(
        "character/move/down/5", Tilesets.CharacterSpriteSheet, (48 * 5, 48 * 4), is_character=True
    )
    CharacterMoveDown6 = register(
        "character/move/down/6", Tilesets.CharacterSpriteSheet, (48 * 6, 48 * 4), is_character=True
    )
    CharacterMoveDown7 = register(
        "character/move/down/7", Tilesets.CharacterSpriteSheet, (48 * 7, 48 * 4), is_character=True
    )

    CharacterMoveLeft0 = register(
        "character/move/left/0", Tilesets.CharacterSpriteSheet, (48 * 0, 48 * 7), is_character=True
    )
    CharacterMoveLeft1 = register(
        "character/move/left/1", Tilesets.CharacterSpriteSheet, (48 * 1, 48 * 7), is_character=True
    )
    CharacterMoveLeft2 = register(
        "character/move/left/2", Tilesets.CharacterSpriteSheet, (48 * 2, 48 * 7), is_character=True
    )
    CharacterMoveLeft3 = register(
        "character/move/left/3", Tilesets.CharacterSpriteSheet, (48 * 3, 48 * 7), is_character=True
    )
    CharacterMoveLeft4 = register(
        "character/move/left/4", Tilesets.CharacterSpriteSheet, (48 * 4, 48 * 7), is_character=True
    )
    CharacterMoveLeft5 = register(
        "character/move/left/5", Tilesets.CharacterSpriteSheet, (48 * 5, 48 * 7), is_character=True
    )
    CharacterMoveLeft6 = register(
        "character/move/left/6", Tilesets.CharacterSpriteSheet, (48 * 6, 48 * 7), is_character=True
    )
    CharacterMoveLeft7 = register(
        "character/move/left/7", Tilesets.CharacterSpriteSheet, (48 * 7, 48 * 7), is_character=True
    )
