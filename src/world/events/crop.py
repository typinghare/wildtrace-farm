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
from src.world.item.crop import GameCrop


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
