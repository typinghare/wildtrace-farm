import pygame

from src.core.context import Context
from src.world.context_getters import get_shopping, get_character, get_hotbar, get_data_window
from src.world.shopping import Shopping


def init_shopping(context: Context) -> None:
    """
    Initializes shopping module.
    """
    context["shopping"] = Shopping(context)


def update_shopping(context: Context) -> None:
    """
    Updates shopping module.
    """
    get_shopping(context).update()


def shopping_key_down(context: Context) -> None:
    """
    Shopping related keydown event.
    """
    key = context.event_data.get("key")
    shopping = get_shopping(context)
    character = get_character(context)

    if key == pygame.K_w:
        shopping.move_up()
    elif key == pygame.K_s:
        shopping.move_down()
    elif key == pygame.K_c:
        shopping.close()
        character.frozen = False
    elif key == pygame.K_b:
        selected_product = shopping.get_selected_product()

        # Check current money
        data_window = get_data_window(context)
        current_money = data_window.money
        if current_money < selected_product.price:
            return

        # Deduct money
        data_window.money -= selected_product.price

        # Adds an item to the hotbar
        hotbar = get_hotbar(context)
        hotbar.chest.stack_item(selected_product.item, 1)
