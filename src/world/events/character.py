"""
Character related events.
"""
import pygame

from src.core.constant import Direction
from src.core.context import Context
from src.core.display import GridLayer
from src.world.character import Character
from src.world.context_getters import get_character, get_data_window
from src.world.data.frames import Frames
from src.world.data.items import ItemTags
from src.world.data.maps import Maps
from src.world.data.registries import Registries
from src.world.data.tiles import Tiles
from src.world.data_window import DataWindow
from src.world.events.game import first_time_to_farm
from src.world.hotbar import Hotbar
from src.world.item.item import GameItem
from src.world.maps.farm import FarmMap
from src.world.maps.home import HomeMap
from src.world.message_box import MessageBox
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
        # Yield to the message box
        message_box: MessageBox = context["message_box"]
        if message_box.is_displayed():
            return

        if character_open_door(context):
            return
        if character_use_item(context):
            return
        if character_sleep(context):
            return


def is_tilled_dirt_cell(cell: GridLayer.Cell) -> bool:
    """
    Checks whether a cell is tilled dirt cell.
    """
    # return cell.surface in Renderers.TilledDirt.tiles
    return cell.surface == Tiles.TilledDirt15


def character_use_item(context: Context) -> bool:
    """
    Character uses item.
    """
    character: Character = context["character"]
    coordinate = character.get_coordinate()
    hotbar: Hotbar = context["hotbar"]
    selected_item: GameItem | None = hotbar.get_selected_item()

    if selected_item is None:
        # Nothing can be used
        return False

    item_ref = Registries.Item.get_ref_by_res(selected_item.item)

    if item_ref.contain_tag(ItemTags.TOOL):
        # Tools
        pass
    elif item_ref.contain_tag(ItemTags.SEEDS):
        # Sow seeds
        scene_manager: SceneManager = context["scene_manager"]

        # Check whether the current map is farm
        if scene_manager.current_map != Maps.Farm.__class__:
            return False

        # Check whether the cell is arable
        farm_map: FarmMap = scene_manager.controller.map
        if (
            not is_tilled_dirt_cell(farm_map.floor.get_cell(coordinate))
            or farm_map.crop.get_cell(coordinate).surface is not None
        ):
            return False

        # Sow seeds: consume a packet of seeds; update the crop layer
        hotbar.consume_selected_item()
        farm_map.crop.update_cell(coordinate, Tiles.WheatSeedling)

        return True

    return False


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
            if index != count - 1:
                # Only update the door frame
                home_map.furniture_bottom.wipe_cell(door_coordinate)
                home_map.furniture_bottom.update_cell(door_coordinate, door_frames[index])
                return

            # Get out to the farm
            def to_farm():
                character.teleport((19, 7))
                character.facing = Direction.DOWN
                character.stop_all()

                if not context["flag.been_to_farm"]:
                    first_time_to_farm(context)

            scene_manager.load_map(Maps.Farm, to_farm)
            home_map.furniture_bottom.update_cell(door_coordinate, Tiles.Door5)

        context.loop_manager.once(10, count, door_loop)
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
            if index != count - 1:
                farm_map.furniture_bottom.wipe_cell(door_coordinate)
                farm_map.furniture_bottom.update_cell(door_coordinate, door_frames[index])
                return

            # Get into the house
            def back_home():
                character.teleport((4, 4))
                character.facing = Direction.UP
                character.stop_all()

            scene_manager.load_map(Maps.Home, back_home)
            farm_map.furniture_bottom.update_cell(door_coordinate, Tiles.Door5)

        context.loop_manager.once(10, count, door_loop)
        return True

    return False


def character_sleep(context: Context) -> bool:
    """
    Character sleeps.
    """
    character: Character = context["character"]
    scene_manager: SceneManager = context["scene_manager"]

    if not scene_manager.is_map(Maps.Home):
        return False

    coordinate = character.get_coordinate()
    if not coordinate == (2, 4) or not character.facing == Direction.LEFT:
        return False

    # Sleep
    transition_to_next_day(context)

    return True


def transition_to_next_day(context: Context) -> None:
    """
    Transits to the next day.
    """
    data_window = get_data_window(context)
    character = get_character(context)
    loop_manager = context.loop_manager
    curtain = context["curtain"]
    fade_speed: int = 25

    def delay():
        # Delay 1.5 seconds
        loop_manager.delay(1500, callback)

    def callback():
        # Set the data window
        data_window.day += 1
        data_window.reset_time()
        character.facing = Direction.RIGHT

        curtain.fade_in(25)

    curtain.fade_out(fade_speed, delay)


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
