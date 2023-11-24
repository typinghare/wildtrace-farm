"""
Frame sequence resource modules.
"""
from typing import List
from pygame import Surface

from src.core.common import ListWrapper
from src.registry import RegistryUtil
from src.world.data.registries import Registries
from src.world.data.tiles import Tiles
from src.world.data.sprites import Sprites


def register(path: str, frames: List[Surface]) -> ListWrapper:
    """
    Register a frame sequence.
    :param path: The path of the frame sequence.
    :param frames: A sequence of surfaces.
    :return: The animation.
    """
    res = ListWrapper(frames)
    return Registries.Frames.register(RegistryUtil.createRegistry(path), res)


class Frames:
    """
    Animation frame resources.
    """

    # Character
    CharacterIdleUp = register(
        "character/idle/up",
        [
            Sprites.CharacterIdleUp0,
            Sprites.CharacterIdleUp1,
            Sprites.CharacterIdleUp2,
            Sprites.CharacterIdleUp3,
            Sprites.CharacterIdleUp4,
            Sprites.CharacterIdleUp5,
            Sprites.CharacterIdleUp6,
            Sprites.CharacterIdleUp7,
        ],
    )
    CharacterIdleRight = register(
        "character/idle/right",
        [
            Sprites.CharacterIdleRight0,
            Sprites.CharacterIdleRight1,
            Sprites.CharacterIdleRight2,
            Sprites.CharacterIdleRight3,
            Sprites.CharacterIdleRight4,
            Sprites.CharacterIdleRight5,
            Sprites.CharacterIdleRight6,
            Sprites.CharacterIdleRight7,
        ],
    )
    CharacterIdleDown = register(
        "character/idle/down",
        [
            Sprites.CharacterIdleDown0,
            Sprites.CharacterIdleDown1,
            Sprites.CharacterIdleDown2,
            Sprites.CharacterIdleDown3,
            Sprites.CharacterIdleDown4,
            Sprites.CharacterIdleDown5,
            Sprites.CharacterIdleDown6,
            Sprites.CharacterIdleDown7,
        ],
    )
    CharacterIdleLeft = register(
        "character/idle/left",
        [
            Sprites.CharacterIdleLeft0,
            Sprites.CharacterIdleLeft1,
            Sprites.CharacterIdleLeft2,
            Sprites.CharacterIdleLeft3,
            Sprites.CharacterIdleLeft4,
            Sprites.CharacterIdleLeft5,
            Sprites.CharacterIdleLeft6,
            Sprites.CharacterIdleLeft7,
        ],
    )
    CharacterMoveUp = register(
        "character/move/up",
        [
            Sprites.CharacterMoveUp0,
            Sprites.CharacterMoveUp1,
            Sprites.CharacterMoveUp2,
            Sprites.CharacterMoveUp3,
            Sprites.CharacterMoveUp4,
            Sprites.CharacterMoveUp5,
            Sprites.CharacterMoveUp6,
            Sprites.CharacterMoveUp7,
        ],
    )
    CharacterMoveRight = register(
        "character/move/right",
        [
            Sprites.CharacterMoveRight0,
            Sprites.CharacterMoveRight1,
            Sprites.CharacterMoveRight2,
            Sprites.CharacterMoveRight3,
            Sprites.CharacterMoveRight4,
            Sprites.CharacterMoveRight5,
            Sprites.CharacterMoveRight6,
            Sprites.CharacterMoveRight7,
        ],
    )
    CharacterMoveDown = register(
        "character/move/down",
        [
            Sprites.CharacterMoveDown0,
            Sprites.CharacterMoveDown1,
            Sprites.CharacterMoveDown2,
            Sprites.CharacterMoveDown3,
            Sprites.CharacterMoveDown4,
            Sprites.CharacterMoveDown5,
            Sprites.CharacterMoveDown6,
            Sprites.CharacterMoveDown7,
        ],
    )
    CharacterMoveLeft = register(
        "character/move/left",
        [
            Sprites.CharacterMoveLeft0,
            Sprites.CharacterMoveLeft1,
            Sprites.CharacterMoveLeft2,
            Sprites.CharacterMoveLeft3,
            Sprites.CharacterMoveLeft4,
            Sprites.CharacterMoveLeft5,
            Sprites.CharacterMoveLeft6,
            Sprites.CharacterMoveLeft7,
        ],
    )

    Water = register("water", [Tiles.Water0, Tiles.Water1, Tiles.Water2, Tiles.Water3])

    # Building
    Door = register(
        "door", [Tiles.Door0, Tiles.Door1, Tiles.Door2, Tiles.Door3, Tiles.Door4, Tiles.Door5]
    )
