"""
Character related events.
"""
import pygame

from src.core.constant import Direction
from src.core.context import Context
from src.world.character import Character
from src.world.data.frames import Frames
from src.world.data.maps import Maps
from src.world.data.tiles import Tiles
from src.world.maps.farm import FarmMap
from src.world.maps.home import HomeMap
from src.world.scene_manager import SceneManager


def init_character(context: Context):
    """
    Initializes character.
    """
    context["character"] = Character(context)


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
        if character_open_door(context):
            return
        if character_use_item(context):
            return


def character_use_item(context: Context) -> bool:
    """
    Character uses item.
    """
    character: Character = context["character"]

    return True


def character_open_door(context: Context) -> bool:
    """
    Character opens door.
    """

    character: Character = context["character"]
    scene_manager: SceneManager = context["scene_manager"]
    current_map = scene_manager.current_map
    coordinate = character.get_coordinate()

    if (
        current_map == Maps.Home.__class__
        and character.facing == Direction.DOWN
        and coordinate == (4, 4)
    ):
        home_map: HomeMap = scene_manager.controller.map
        door_coordinate = home_map.door_coordinate
        door_frames = Frames.Door.list
        count = len(door_frames) + 1

        def door_loop(index: int):
            if index == count - 1:
                context.loop_manager.remove(loop)

                # Get out to the farm
                def to_farm():
                    character.teleport((19, 7))
                    character.facing = Direction.DOWN
                    character.stop_all()

                scene_manager.load_map(Maps.Farm, to_farm)
                home_map.furniture_bottom.update_cell(door_coordinate, Tiles.Door5)
            else:
                home_map.furniture_bottom.wipe_cell(door_coordinate)
                home_map.furniture_bottom.update_cell(door_coordinate, door_frames[index])

        loop = context.loop_manager.register(10, count, door_loop)
        return True

    if (
        current_map == Maps.Farm.__class__
        and character.facing == Direction.UP
        and coordinate == (19, 7)
    ):
        farm_map: FarmMap = scene_manager.controller.map
        door_coordinate = farm_map.get_door_coordinate()
        door_frames = Frames.Door.list
        count = len(door_frames) + 1

        def door_loop(index: int):
            if index == count - 1:
                context.loop_manager.remove(loop)

                # Get into the house
                def back_home():
                    character.teleport((4, 4))
                    character.facing = Direction.UP
                    character.stop_all()

                scene_manager.load_map(Maps.Home, back_home)
                farm_map.furniture_bottom.update_cell(door_coordinate, Tiles.Door5)
            else:
                farm_map.furniture_bottom.wipe_cell(door_coordinate)
                farm_map.furniture_bottom.update_cell(door_coordinate, door_frames[index])

        loop = context.loop_manager.register(10, count, door_loop)
        return True

    return False


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
