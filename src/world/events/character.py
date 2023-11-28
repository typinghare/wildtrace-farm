"""
Character related events.
"""
import pygame

from src.core.constant import Direction
from src.core.context import Context
from src.world.character import Character
from src.world.data.maps import Maps
from src.world.scene_manager import SceneManager


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

    # Direction
    direction = map_key_to_direction(key)
    if direction is not None:
        character.move(direction)
        return

    # <J> use item / open doors
    if key == pygame.K_j:
        # use item

        # open doors
        scene_manager: SceneManager = context["scene_manager"]
        current_map = scene_manager.current_map
        coordinate = character.get_coordinate()

        if (
            current_map == Maps.Home.__class__
            and character.facing == Direction.DOWN
            and coordinate == (4, 4)
        ):
            # Get out to the farm
            def to_farm():
                character.teleport((19, 7))
                character.facing = Direction.DOWN
                character.stop_all()

            scene_manager.load_map(Maps.Farm, to_farm)
            return

        if (
            current_map == Maps.Farm.__class__
            and character.facing == Direction.UP
            and coordinate == (19, 7)
        ):
            # Get into the house
            def back_home():
                character.teleport((4, 4))
                character.facing = Direction.UP
                character.stop_all()

            scene_manager.load_map(Maps.Home, back_home)
            return


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
