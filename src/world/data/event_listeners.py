"""
Event listener source module.
"""
from typing import Callable, cast

import pygame

from src.registry import RegistryUtil
from src.core.context import Context
from src.core.event import EventListener
from src.core.constant import EventTypes
from src.world.data.registries import Registries
from src.world.events.initial import init_layer, init_debug, init_water
from src.world.events.window import quit_game, update_loops
from src.world.events.character import init_character, character_key_up, character_key_down


def register(event_type: int, callback: Callable[[Context | None], None]) -> EventListener:
    """
    Registers an event listener.
    :param event_type:
    :param callback:
    :return: The event listener.
    """
    loc = RegistryUtil.createLoc(callback.__name__)
    event_listener = EventListener(event_type, callback)
    return cast(
        EventListener,
        Registries.EventListener.register(loc, event_listener),
    )


class EventListeners:
    """
    Event listener resources.
    """

    # On quit
    QuitGame = register(pygame.QUIT, quit_game)

    # On start
    InitLayer = register(EventTypes.ON_START, init_layer)
    InitDebug = register(EventTypes.ON_START, init_debug)
    InitCharacter = register(EventTypes.ON_START, init_character)
    InitWater = register(EventTypes.ON_START, init_water)

    # Before render
    UpdateLoops = register(EventTypes.BEFORE_RENDER, update_loops)

    # Character movements
    CharacterKeyDown = register(pygame.KEYDOWN, character_key_down)
    CharacterKeyUp = register(pygame.KEYUP, character_key_up)
