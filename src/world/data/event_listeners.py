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
from src.world.data.events.initial import fill_screen_with_grass, init_water
from src.world.data.events.window import quit_game


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

    QuitGame = register(pygame.QUIT, quit_game)
    FillScreenWithGrass = register(EventTypes.ON_START, fill_screen_with_grass)
    InitWater = register(EventTypes.ON_START, init_water)
