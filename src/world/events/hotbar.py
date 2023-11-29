"""
Hotbar related functions.
"""

import pygame

from src.core.context import Context
from src.world.data.items import Items
from src.world.hotbar import Hotbar


def init_hotbar(context: Context) -> None:
    """
    Initializes a hotbar.
    """
    # layer
    hotbar = context["hotbar"] = Hotbar(context)
    hotbar.add_item(Items.WateringCan)
    hotbar.add_item(Items.Hoe)
    hotbar.get_item(1).increase_stack()


def update_hotbar(context: Context) -> None:
    """
    Updates the hotbar.
    """
    hotbar: Hotbar = context["hotbar"]
    hotbar.update()


def hotbar_key_down(context: Context) -> None:
    """
    Hotbar key down. Keys 0 ~ 9 are used to select items.
    """
    key = context.event_data["key"]

    if pygame.K_0 <= key <= pygame.K_9:
        index: int = key - pygame.K_1
        if index == -1:
            index = 9

        hotbar: Hotbar = context["hotbar"]
        hotbar.select_item(index)
