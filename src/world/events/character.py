"""
Character related events.
"""
import pygame

from src.core.context import Context
from src.world.character import Character


def init_character(context: Context):
    """
    Initializes character.
    """
    character: Character = context.set("character", Character(context))
    character.init_animation()


def map_key_to_direction(key: int) -> int | None:
    if key == pygame.K_w:
        return Character.Direction.UP
    if key == pygame.K_d:
        return Character.Direction.RIGHT
    if key == pygame.K_s:
        return Character.Direction.DOWN
    if key == pygame.K_a:
        return Character.Direction.LEFT

    return None


def character_key_down(context: Context):
    """
    Player presses key down when they control the character.
    """
    key = context.event_data["key"]
    character: Character = context.get("character")

    direction = map_key_to_direction(key)
    if direction is not None:
        character.move(direction)


def character_key_up(context: Context):
    """
    Player presses key up when they control the character.
    """
    key = context.event_data["key"]
    character: Character = context.get("character")

    direction = map_key_to_direction(key)
    if direction is not None:
        character.stop(direction)
