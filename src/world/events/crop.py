"""
Crop related functions.
"""
from src.core.common import Grid
from src.core.context import Context
from src.world.context_getters import (
    get_crop_window,
    get_character,
    get_scene_manager,
    get_crop_grid,
)
from src.world.crop_window import CropWindow
from src.world.data.maps import Maps
from src.world.data.tiles import Tiles
from src.world.item.crop import GameCrop
from src.world.maps.farm import FarmMap


def init_crop(context: Context) -> None:
    """
    Initializes crop window and crop grid.
    """
    context["crop_window"] = CropWindow(context)
    context["crop_grid"] = Grid(Maps.Farm.size)


def update_crop_window(context: Context) -> None:
    """
    Updates the crop window.
    """
    scene_manager = get_scene_manager(context)
    if not scene_manager.is_map(Maps.Farm):
        return

    character = get_character(context)
    coordinate = character.get_coordinate()
    crop_grid = get_crop_grid(context)
    crop: GameCrop | None = crop_grid.get(coordinate)

    crop_window = get_crop_window(context)
    if crop is None:
        crop_window.hide()

    crop_window.display_crop_info(crop)


def update_crop(context: Context) -> None:
    crop_grid = get_crop_grid(context)
    scene_manager = get_scene_manager(context)
    farm_map: FarmMap = scene_manager.get_map_controller(Maps.Farm).map
    for row in range(crop_grid.size.height):
        for col in range(crop_grid.size.width):
            coordinate = (col, row)
            game_crop: GameCrop | None = crop_grid.get(coordinate)
            if game_crop is None:
                continue

            # Update crop status
            is_watered = game_crop.watered
            game_crop.day += 1 if is_watered else 0.5

            # Reset watered
            game_crop.watered = False

            # Update the crop layer
            farm_map.crop.update_cell(coordinate, game_crop.image)

    for row in range(farm_map.size.height):
        for col in range(farm_map.size.width):
            coordinate = (col, row)
            if farm_map.floor.get_cell(coordinate).surface == Tiles.DarkenTilledDirt15:
                farm_map.floor.update_cell(coordinate, Tiles.TilledDirt15)
