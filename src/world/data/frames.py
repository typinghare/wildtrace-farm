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

    CharacterWaterUp = register(
        "character/water/up",
        [
            Sprites.CharacterWaterUp0,
            Sprites.CharacterWaterUp1,
            Sprites.CharacterWaterUp2,
            Sprites.CharacterWaterUp3,
            Sprites.CharacterWaterUp4,
            Sprites.CharacterWaterUp5,
            Sprites.CharacterWaterUp6,
            Sprites.CharacterWaterUp7,
        ],
    )
    CharacterWaterRight = register(
        "character/water/right",
        [
            Sprites.CharacterWaterRight0,
            Sprites.CharacterWaterRight1,
            Sprites.CharacterWaterRight2,
            Sprites.CharacterWaterRight3,
            Sprites.CharacterWaterRight4,
            Sprites.CharacterWaterRight5,
            Sprites.CharacterWaterRight6,
            Sprites.CharacterWaterRight7,
        ],
    )
    CharacterWaterDown = register(
        "character/water/down",
        [
            Sprites.CharacterWaterDown0,
            Sprites.CharacterWaterDown1,
            Sprites.CharacterWaterDown2,
            Sprites.CharacterWaterDown3,
            Sprites.CharacterWaterDown4,
            Sprites.CharacterWaterDown5,
            Sprites.CharacterWaterDown6,
            Sprites.CharacterWaterDown7,
        ],
    )
    CharacterWaterLeft = register(
        "character/water/left",
        [
            Sprites.CharacterWaterLeft0,
            Sprites.CharacterWaterLeft1,
            Sprites.CharacterWaterLeft2,
            Sprites.CharacterWaterLeft3,
            Sprites.CharacterWaterLeft4,
            Sprites.CharacterWaterLeft5,
            Sprites.CharacterWaterLeft6,
            Sprites.CharacterWaterLeft7,
        ],
    )

    # Character actions
    Watering = register(
        "watering",
        [
            Sprites.Watering0,
            Sprites.Watering1,
            Sprites.Watering2,
            Sprites.Watering3,
            Sprites.Watering4,
            Sprites.Watering5,
            Sprites.Watering6,
            Sprites.Watering7,
            Sprites.Watering8,
        ],
    )

    Water = register("water", [Tiles.Water0, Tiles.Water1, Tiles.Water2, Tiles.Water3])

    # Building
    Door = register(
        "door", [Tiles.Door5, Tiles.Door4, Tiles.Door3, Tiles.Door2, Tiles.Door1, Tiles.Door0]
    )
    Chest = register(
        "chest",
        [
            Tiles.ChestFront0,
            Tiles.ChestFront1,
            Tiles.ChestFront2,
            Tiles.ChestFront3,
            Tiles.ChestFront4,
        ],
    )
