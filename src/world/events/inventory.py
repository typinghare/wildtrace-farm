"""
Inventory related functions.
"""
import pygame

from src.core.constant import Direction
from src.core.context import Context
from src.world.context_getters import  get_inventory, get_character
from src.world.item.inventory import Inventory


def init_inventory(context: Context) -> None:
    """
    Initializes the inventory.
    """
    context["inventory"] = Inventory(context)


def update_inventory(context: Context) -> None:
    """
    Updates the inventory.
    """
    get_inventory(context).update()


def inventory_key_down(context: Context) -> None:
    """
    Inventory key down.
    """
    key: int = context.event_data["key"]
    inventory = get_inventory(context)
    chest = inventory.chest

    if not inventory.displayed or chest is None:
        return

    chest_num_col = chest.size.width
    chest_num_row = chest.size.height
    chest_selected_index = chest.get_selected_index()

    if key == pygame.K_c:
        # Close the inventory
        inventory.close_chest()

        # Unfreeze the character
        character = get_character(context)
        character.frozen = False
        character.facing = Direction.UP
    elif key == pygame.K_w:
        index = chest_selected_index - chest_num_col
        if index > 0:
            chest.select_item(index)
    elif key == pygame.K_d:
        if (1 + chest_selected_index % chest_num_col) != 0:
            chest.select_item(chest_selected_index + 1)
    elif key == pygame.K_s:
        index = chest_selected_index + chest_num_col
        if index < chest_num_col * chest_num_row:
            chest.select_item(index)
    elif key == pygame.K_a:
        if chest_selected_index % chest_num_col != 0:
            chest.select_item(chest_selected_index - 1)
    elif key == pygame.K_n:
        # Move item from the hotbar to the inventory
        pass
    elif key == pygame.K_m:
        # Move item from the inventory to the hotbar
        pass
