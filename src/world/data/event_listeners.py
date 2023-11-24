"""
Event listener resource module.
"""
from typing import Callable, cast

import pygame

from src.registry import RegistryUtil
from src.core.context import Context
from src.core.event import EventListener
from src.core.constant import EventTypes
from src.world.data.registries import Registries
from src.world.events.init import init_map, init_debug
from src.world.events.window import quit_game, update_loops
from src.world.events.character import (
    init_character,
    character_key_up,
    character_key_down,
    update_character,
)
from src.world.events.map import update_map


def register(event_type: int, callback: Callable[[Context | None], None]) -> EventListener:
    """
    Registers an event listener.
    :param event_type: The type of event to listen for.
    :param callback: The callback function to be called when the event is triggered.
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
    InitLayer = register(EventTypes.ON_START, init_map)
    InitDebug = register(EventTypes.ON_START, init_debug)
    InitCharacter = register(EventTypes.ON_START, init_character)

    # Before render
    UpdateLoops = register(EventTypes.BEFORE_RENDER, update_loops)
    UpdateMap = register(EventTypes.BEFORE_RENDER, update_map)
    UpdateCharacter = register(EventTypes.BEFORE_RENDER, update_character)

    # Character movements
    CharacterKeyDown = register(pygame.KEYDOWN, character_key_down)
    CharacterKeyUp = register(pygame.KEYUP, character_key_up)
