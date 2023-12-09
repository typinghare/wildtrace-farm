"""
Character related events.
"""
from typing import Dict, Callable, List

import pygame

from src.core.constant import Direction
from src.core.context import Context
from src.core.display import GridLayer
from src.registry import RegistryUtil
from src.world.character import Character
from src.core.common.methodical import CallbackQueue, CallbackNode
from src.world.context_getters import (
    get_character,
    get_data_window,
    get_curtain,
    get_scene_manager,
    get_inventory,
    get_message_box,
    get_crop_grid,
    get_hotbar,
    get_music,
)
from src.world.data.frames import Frames
from src.world.data.items import ItemTags, Items
from src.world.data.maps import Maps
from src.world.data.music import Music
from src.world.data.registries import Registries
from src.world.data.tiles import Tiles
from src.world.events.crop import update_crop
from src.world.events.game import first_time_to_farm
from src.world.item.chest import Chest
from src.world.item.crop import Crop, GameCrop
from src.world.item.hotbar import Hotbar
from src.world.item.item import GameItem, Item
from src.world.item.product import Product
from src.world.map import Map
from src.world.maps.farm import FarmMap
from src.world.maps.home import HomeMap
from src.world.message_box import MessageBox
from src.world.scene_manager import SceneManager
from src.world.util import flip_coin


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

    # Yield to the message box
    message_box: MessageBox = get_message_box(context)
    if message_box.is_displayed():
        return

    # Direction
    direction = map_key_to_direction(key)
    if direction is not None:
        character.move(direction)
        return

    # <J> use item / open doors / sleep / open inventory
    if key == pygame.K_j:
        if character_open_door(context):
            return
        if character_sleep(context):
            return
        if character_open_chest(context):
            return
        if character_harvest_crop(context):
            return
        if character_use_item(context):
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
    selected_item: GameItem | None = hotbar.chest.get_selected_item()

    if selected_item is None:
        # Nothing can be used
        return False

    item_ref = Registries.Item.get_ref_by_res(selected_item.item)

    if item_ref.contain_tag(ItemTags.TOOL):
        # Tools
        if selected_item.item == Items.WateringCan:
            return character_use_watering_can(context, character)
    elif item_ref.contain_tag(ItemTags.SEEDS):
        # Sow seeds
        scene_manager: SceneManager = context["scene_manager"]

        # Check whether the current map is farm
        if not scene_manager.is_map(Maps.Farm):
            return False

        # Check whether the cell is arable
        farm_map: FarmMap = scene_manager.controller.map
        if (
            not is_tilled_dirt_cell(farm_map.floor.get_cell(coordinate))
            or farm_map.crop.get_cell(coordinate).surface is not None
        ):
            return False

        # Sow seeds: consume a packet of seeds; update the crop layer
        hotbar.chest.consume_selected_item()
        crop_item_mapping: Dict[Item, Crop] = context["crop_item_mapping"]
        crop: Crop | None = crop_item_mapping.get(selected_item.item)
        if crop is None:
            return False

        game_crop = GameCrop(crop)
        crop_grid = get_crop_grid(context)
        crop_grid.set(coordinate, game_crop)
        farm_map.crop.update_cell(coordinate, game_crop.image)

        return True

    return False


def character_use_watering_can(context: Context, character: Character) -> bool:
    """
    Character uses the watering can.
    """
    scene_manager = get_scene_manager(context)
    if not scene_manager.is_map(Maps.Farm):
        return False

    coordinate = character.get_coordinate()
    character_fps = context.settings.character_animation_fps

    # Play watering animation
    scene_manager = get_scene_manager(context)
    animation_layer = GridLayer(
        scene_manager.controller.map.size, context.settings.display_cell_size
    )
    context.display.set_layer("animation", animation_layer)
    watering_frames = Frames.Watering.list

    def update_watering_animation(index: int) -> None:
        if index == len(watering_frames):
            animation_layer.wipe_cell(coordinate)
            return

        animation_layer.wipe_cell(coordinate)
        animation_layer.update_cell(coordinate, watering_frames[index])

    context.loop_manager.once(character_fps, len(watering_frames) + 1, update_watering_animation)

    # Character animation
    character.set_action(Character.Action.Water)
    context.loop_manager.delay(
        1000 / character_fps * 9,
        lambda: character.set_action(Character.Action.Idle),
    )

    # Update the corresponding game crop
    crop_grid = get_crop_grid(context)
    game_crop: GameCrop | None = crop_grid.get(coordinate)
    if game_crop:
        game_crop.watered = True

    # Update floor
    farm_map: FarmMap = scene_manager.get_map_controller(Maps.Farm).map
    if farm_map.floor.get_cell(coordinate).surface == Tiles.TilledDirt15:
        farm_map.floor.update_cell(coordinate, Tiles.DarkenTilledDirt15)

    return True


def character_open_door(context: Context) -> bool:
    """
    Character opens door.
    """
    if context["flag.door_opening"]:
        return True

    character: Character = context["character"]
    scene_manager: SceneManager = context["scene_manager"]
    coordinate = character.get_coordinate()

    if (
        scene_manager.is_map(Maps.Home)
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
                home_map.furniture_bottom.wipe_cell(door_coordinate, 255)
                home_map.furniture_bottom.update_cell(door_coordinate, door_frames[index])
                return

            # Get out to the farm
            def to_farm():
                character.teleport((19, 7))
                character.facing = Direction.DOWN
                character.stop_all()
                character.frozen = False

                # Stop music and play another music
                if flip_coin() or not context["flag.been_to_farm"]:
                    music = get_music(context)
                    if not music.is_playing():
                        get_music(context).fade_in(Music.Farm)

                if not context["flag.been_to_farm"]:
                    first_time_to_farm(context)

            scene_manager.change_map(Maps.Farm, to_farm)
            home_map.furniture_bottom.update_cell(door_coordinate, Tiles.Door5)
            context["flag.door_opening"] = False

        character.frozen = True
        context["flag.door_opening"] = True
        context.loop_manager.once(10, count, door_loop)
        return True

    if (
        scene_manager.is_map(Maps.Farm)
        and character.facing == Direction.UP
        and coordinate == (19, 7)
    ):
        farm_map: FarmMap = scene_manager.controller.map
        door_coordinate = farm_map.get_door_coordinate()
        door_frames = Frames.Door.list
        count = len(door_frames) + 1
        up_coordinate = (door_coordinate[0], door_coordinate[1] - 1)

        def door_loop(index: int):
            if index != count - 1:
                farm_map.ground.wipe_cell(door_coordinate)
                farm_map.ground.update_cell(door_coordinate, door_frames[index])
                farm_map.floor.update_cell(up_coordinate, Tiles.WoodenHouse13)

                return

            # Get into the house
            def back_home():
                character.teleport((4, 4))
                character.facing = Direction.UP
                character.stop_all()
                character.frozen = False

            scene_manager.change_map(Maps.Home, back_home)
            farm_map.floor.update_cell(up_coordinate, Tiles.WoodenHouse13)
            farm_map.ground.update_cell(door_coordinate, Tiles.Door5)

            context["flag.door_opening"] = False

        character.frozen = True
        context["flag.door_opening"] = True
        context.loop_manager.once(10, count, door_loop)
        return True

    return False


def character_sleep(context: Context) -> bool:
    """
    Character sleeps.
    """
    character: Character = context["character"]
    scene_manager: SceneManager = context["scene_manager"]

    # Reject any requests if the character is sleeping
    if context["flag.sleeping"]:
        return True

    if not scene_manager.is_map(Maps.Home):
        return False

    coordinate = character.get_coordinate()
    if not coordinate == (2, 4) or not character.facing == Direction.LEFT:
        return False

    # Sleep
    context["flag.sleeping"] = True
    character.frozen = True
    transition_to_next_day(context)

    return True


def character_open_chest(context: Context) -> bool:
    """
    Character opens a chest.
    """
    scene_manager = get_scene_manager(context)
    character = get_character(context)
    inventory = get_inventory(context)
    front_coordinate = character.get_front_coordinate()

    def check_chest(_map: Map, chest: Chest) -> bool:
        if not scene_manager.is_map(_map):
            return False

        concrete_map = scene_manager.controller.map
        furniture_bottom_layer: GridLayer = concrete_map.furniture_bottom
        floor_layer: GridLayer = concrete_map.floor

        if furniture_bottom_layer.get_cell(front_coordinate).surface != Tiles.ChestFront0:
            return False

        frames = Frames.Chest.list
        num_frame: int = len(frames)
        floor_cell = floor_layer.get_cell(front_coordinate)

        def after_animation() -> None:
            character.frozen = True
            character.stop_all()
            inventory.open_chest(chest)

        def chest_animation(index: int):
            if index < num_frame:
                furniture_bottom_layer.wipe_cell(front_coordinate)
                furniture_bottom_layer.update_cell(front_coordinate, frames[index])
                floor_layer.update_cell(front_coordinate, floor_cell.surface)
            else:
                # First open the chest
                if context["flag.first_open_chest"]:
                    first_time_to_open_chest(context, after_animation)
                else:
                    after_animation()

        # Play frames
        context.loop_manager.once(6, num_frame + 1, chest_animation)

        return True

    if check_chest(Maps.Farm, context["shipping_chest"]):
        return True

    if check_chest(Maps.Home, context["home_chest"]):
        return True

    return False


def first_time_to_open_chest(context: Context, callback: Callable) -> None:
    context["flag.first_open_chest"] = False
    message_box = get_message_box(context)

    def fn0() -> CallbackNode:
        lines = [
            "Looks like this is your first time using a chest.",
            "You can press [W][A][S][D] to select items in the chest;",
            "Press [N] to move the selected item to the chest;",
            "Press [M] to move the selected item to the hotbar;",
            "Press [C] to close the chest.",
        ]
        return message_box.play("\n".join(lines))

    CallbackQueue([fn0, callback]).start()


def transition_to_next_day(context: Context) -> None:
    """
    Transits to the next day.
    """
    data_window = get_data_window(context)
    character = get_character(context)
    curtain = get_curtain(context)
    loop_manager = context.loop_manager

    get_music(context).fade_out()

    def fn0() -> CallbackNode:
        return curtain.fade_out(context.settings.sleep_fade_speed)

    def fn1() -> CallbackNode | None:
        return shipping(context)

    def fn2() -> CallbackNode:
        return loop_manager.delay_methodical(1000)

    def fn3() -> CallbackNode:
        # Set the data window
        data_window.day += 1
        data_window.reset_time()

        # Update crops
        update_crop(context)

        # Character facing
        character.facing = Direction.RIGHT
        character.frozen = False

        if flip_coin(0.35):
            get_music(context).fade_in(Music.Home)

        return curtain.fade_in(context.settings.sleep_fade_speed)

    def fn4() -> None:
        context["flag.sleeping"] = False

    CallbackQueue([fn0, fn1, fn2, fn3, fn4]).start()


def shipping(context: Context) -> CallbackNode | None:
    """
    Ships all products in the shipping chest.
    """
    shipping_chest: Chest = context["shipping_chest"]

    shipped_products: Dict[int, int] = {}
    for game_item in shipping_chest.item_list:
        if game_item is None:
            continue

        item_ref = Registries.Item.get_ref_by_res(game_item.item)
        loc = item_ref.res_key.loc
        path = loc.path
        if not path.startswith("product/"):
            continue

        # Get product
        product_name = path[8:]
        product_ref = Registries.Product.get_ref(RegistryUtil.createLoc(product_name))
        product_id: int = product_ref.get_id()

        # Aggregate
        number_product = game_item.stack
        if product_id in shipped_products:
            shipped_products[product_id] += number_product
        else:
            shipped_products[product_id] = number_product

    # Calculate total price
    total_price: int = 0
    str_list: List[str] = []
    for product_id, number_product in shipped_products.items():
        product: Product = Registries.Product.by_id[product_id].res
        total_price += product.price * number_product
        str_list.append(
            f"  {product.item.name} - ${product.price}"
            f" * {number_product} = ${product.price * number_product}"
        )

    if total_price == 0:
        return None

    # Update money
    data_window = get_data_window(context)
    data_window.money += total_price

    # Clear all items in the chest
    item_list = shipping_chest.item_list
    for i in range(len(item_list)):
        item_list[i] = None

    # Display price using message box
    message_box = get_message_box(context)

    return message_box.play(
        f"You have shipped the following products:\n"
        + "\n".join(str_list)
        + f"\nYou earned ${total_price}!",
    )


def character_harvest_crop(context: Context) -> bool:
    """
    Character harvests a crop.
    """
    character = get_character(context)
    coordinate = character.get_coordinate()
    scene_manager = get_scene_manager(context)

    if not scene_manager.is_map(Maps.Farm):
        return False

    crop_grid = get_crop_grid(context)
    game_crop: GameCrop | None = crop_grid.get(coordinate)
    if game_crop is None:
        return False

    if game_crop.stage != Crop.Stage.Ripening:
        # Not yet ripen
        return False

    # Harvest logic
    # Remove the crop from the crop grid; update the crop layer
    farm_map: FarmMap = scene_manager.controller.map
    crop_grid.set(coordinate, None)
    farm_map.crop.wipe_cell(coordinate)
    farm_map.crop.update_cell(coordinate, None)

    # Update character hotbar
    hotbar = get_hotbar(context)
    hotbar.chest.stack_item(game_crop.crop.product.item)

    # First time to harvest
    if context["flag.first_time_to_harvest"]:
        context["flag.first_time_to_harvest"] = False
        message_box = get_message_box(context)
        message_box.play(
            "You harvested your first crop!\n"
            "You can put crop products to the chest in the farm.\n"
            "All products will be shipped to town overnight,\n"
            "and they will pay you.\n"
        )


def character_key_up(context: Context):
    """
    Player presses key up when they control the character.
    """
    key = context.event_data.get("key")
    character: Character = context["character"]

    # Yield to the message box
    message_box: MessageBox = get_message_box(context)
    if message_box.is_displayed():
        return

    direction = map_key_to_direction(key)
    if direction is not None:
        character.stop(direction)


def update_character(context: Context):
    """
    Updates character's position.
    """
    character: Character = context["character"]
    character.update()
