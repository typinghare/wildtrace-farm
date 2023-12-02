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
from src.world.events.crop import init_crop, update_crop_window
from src.world.events.curtain import init_curtain, update_curtain
from src.world.events.data_window import init_data_window, update_data_window
from src.world.events.debug import init_debug, update_debug
from src.world.events.game import init_flags, before_all
from src.world.events.inventory import init_inventory, update_inventory, inventory_key_down
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
from src.world.events.hotbar import init_hotbar, update_hotbar, hotbar_key_down


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
    InitFlags = register(EventTypes.ON_START, init_flags)
    InitLayer = register(EventTypes.ON_START, init_layer)
    InitDebug = register(EventTypes.ON_START, init_debug)
    InitCharacter = register(EventTypes.ON_START, init_character)
    InitMap = register(EventTypes.ON_START, init_map)
    InitHotbar = register(EventTypes.ON_START, init_hotbar)
    InitMessageBox = register(EventTypes.ON_START, init_message_box)
    InitDataWindow = register(EventTypes.ON_START, init_data_window)
    InitCurtain = register(EventTypes.ON_START, init_curtain)
    InitInventory = register(EventTypes.ON_START, init_inventory)
    InitCrop = register(EventTypes.ON_START, init_crop)
    BeforeAll = register(EventTypes.ON_START, before_all)

    # Before render
    UpdateDebug = register(EventTypes.BEFORE_RENDER, update_debug)
    UpdateLoops = register(EventTypes.BEFORE_RENDER, update_loops)
    UpdateCharacter = register(EventTypes.BEFORE_RENDER, update_character)
    UpdateMap = register(EventTypes.BEFORE_RENDER, update_map)
    UpdateHotbar = register(EventTypes.BEFORE_RENDER, update_hotbar)
    UpdateMessageBox = register(EventTypes.BEFORE_RENDER, update_message_box)
    UpdateDataWindow = register(EventTypes.BEFORE_RENDER, update_data_window)
    UpdateCurtain = register(EventTypes.BEFORE_RENDER, update_curtain)
    UpdateInventory = register(EventTypes.BEFORE_RENDER, update_inventory)
    UpdateCropWindow = register(EventTypes.BEFORE_RENDER, update_crop_window)

    # Key down
    CharacterKeyDown = register(pygame.KEYDOWN, character_key_down)
    MessageBoxKeyDown = register(pygame.KEYDOWN, message_box_key_down)
    HotbarKeyDown = register(pygame.KEYDOWN, hotbar_key_down)
    InventoryKeyDown = register(pygame.KEYDOWN, inventory_key_down)

    # Key up
    CharacterKeyUp = register(pygame.KEYUP, character_key_up)
