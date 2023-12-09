"""
Inventory related functions.
"""
import pygame

from src.core.constant import Direction
from src.core.context import Context
from src.core.display import GridLayer
from src.world.context_getters import get_inventory, get_character, get_hotbar, get_scene_manager
from src.world.data.frames import Frames
from src.world.item.inventory import Inventory
from src.world.item.item import GameItem


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
    hotbar = get_hotbar(context)
    chest = inventory.chest

    if not inventory.displayed or chest is None:
        return

    chest_num_col = chest.size.width
    chest_selected_index = chest.get_selected_index()

    if key == pygame.K_c:
        close_chest(context)
    elif key == pygame.K_w:
        # Up
        chest.select_item(chest_selected_index - chest_num_col)
    elif key == pygame.K_d:
        # Right
        chest.select_item(chest_selected_index + 1)
    elif key == pygame.K_s:
        # Down
        chest.select_item(chest_selected_index + chest_num_col)
    elif key == pygame.K_a:
        # Left
        chest.select_item(chest_selected_index - 1)
    elif key == pygame.K_n:
        # Move item from the hotbar to the inventory
        hotbar_selected_index: int = hotbar.chest.get_selected_index()
        hotbar_selected_item: GameItem = hotbar.chest.get_selected_item()
        if hotbar_selected_item is None:
            return

        result = chest.append_game_item(hotbar_selected_item)
        if result:
            hotbar.chest.remove_item(hotbar_selected_index)
    elif key == pygame.K_m:
        # Move item from the inventory to the hotbar
        inventory_selected_index: int = chest.get_selected_index()
        inventory_selected_item: GameItem = chest.get_selected_item()
        if inventory_selected_item is None:
            return

        result = hotbar.chest.append_game_item(inventory_selected_item)
        if result:
            chest.remove_item(inventory_selected_index)


def close_chest(context: Context) -> None:
    inventory = get_inventory(context)
    inventory.close_chest()

    # Close chest animation
    character = get_character(context)
    front_coordinate = character.get_front_coordinate()
    frames = Frames.Chest.list[::-1]
    num_frame: int = len(frames)

    scene_manager = get_scene_manager(context)
    concrete_map = scene_manager.controller.map
    furniture_bottom_layer: GridLayer = concrete_map.furniture_bottom
    floor_layer: GridLayer = concrete_map.floor
    floor_cell = floor_layer.get_cell(front_coordinate)

    def chest_animation(index: int):
        if index < num_frame:
            furniture_bottom_layer.wipe_cell(front_coordinate)
            furniture_bottom_layer.update_cell(front_coordinate, frames[index])
            floor_layer.update_cell(front_coordinate, floor_cell.surface)

    context.loop_manager.once(6, num_frame + 1, chest_animation)

    # Unfreeze the character
    character = get_character(context)
    character.frozen = False