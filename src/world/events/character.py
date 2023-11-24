"""
Character related events.
"""
import pygame

from src.core.constant import Direction
from src.core.context import Context
from src.world.character import Character


def init_character(context: Context):
    """
    Initializes character.
    """
    character = context["character"] = Character(context)
    character.init_animation()


def map_key_to_direction(key: int) -> int | None:
    if key == pygame.K_w:
        return Direction.UP
    if key == pygame.K_d:
        return Direction.RIGHT
    if key == pygame.K_s:
        return Direction.DOWN
    if key == pygame.K_a:
        return Direction.LEFT

    return None


def character_key_down(context: Context):
    """
    Player presses key down when they control the character.
    """
    key = context.event_data.get("key")
    character: Character = context["character"]

    direction = map_key_to_direction(key)
    if direction is not None:
        character.move(direction)


def character_key_up(context: Context):
    """
    Player presses key up when they control the character.
    """
    key = context.event_data.get("key")
    character: Character = context["character"]

    direction = map_key_to_direction(key)
    if direction is not None:
        character.stop(direction)


def update_character(context: Context):
    """
    Updates character's position.
    """
    character: Character = context["character"]
    character.update()
