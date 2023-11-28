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
from src.world.events.debug import init_debug, update_debug
from src.world.events.layer import init_layer
from src.world.events.message_box import init_message_box, update_message_box, message_box_key_down
from src.world.events.window import quit_game, update_loops
from src.world.events.character import (
    init_character,
    character_key_up,
    character_key_down,
    update_character,
)
from src.world.events.map import init_map, update_map
from src.world.events.tool import init_tool, update_tool, tool_key_up


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
    InitLayer = register(EventTypes.ON_START, init_layer)
    InitDebug = register(EventTypes.ON_START, init_debug)
    InitCharacter = register(EventTypes.ON_START, init_character)
    InitMap = register(EventTypes.ON_START, init_map)
    InitTool = register(EventTypes.ON_START, init_tool)
    InitMessageBox = register(EventTypes.ON_START, init_message_box)

    # Before render
    UpdateDebug = register(EventTypes.BEFORE_RENDER, update_debug)
    UpdateLoops = register(EventTypes.BEFORE_RENDER, update_loops)
    UpdateCharacter = register(EventTypes.BEFORE_RENDER, update_character)
    UpdateMap = register(EventTypes.BEFORE_RENDER, update_map)
    UpdateTool = register(EventTypes.BEFORE_RENDER, update_tool)
    updateMessageBox = register(EventTypes.BEFORE_RENDER, update_message_box)

    # Key down
    CharacterKeyDown = register(pygame.KEYDOWN, character_key_down)
    MessageBoxKeyDown = register(pygame.KEYDOWN, message_box_key_down)

    # Key up
    CharacterKeyUp = register(pygame.KEYUP, character_key_up)
    ToolKeyUp = register(pygame.KEYUP, tool_key_up)
