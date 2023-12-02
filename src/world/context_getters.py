"""
Context getters module. This module provides a bunch of utility functions that get a value from the
given context.
"""
from src.core.common import Grid
from src.core.context import Context
from src.world.character import Character
from src.world.crop_window import CropWindow
from src.world.curtain import Curtain
from src.world.data_window import DataWindow
from src.world.item.hotbar import Hotbar
from src.world.item.inventory import Inventory
from src.world.message_box import MessageBox
from src.world.scene_manager import SceneManager


def get_character(context: Context) -> Character:
    """
    Returns the character object in the given context.
    """
    return context["character"]


def get_data_window(context: Context) -> DataWindow:
    """
    Returns the data window object in the given context.
    """
    return context["data_window"]


def get_curtain(context: Context) -> Curtain:
    """
    Returns the curtain object in the given context.
    """
    return context["curtain"]


def get_inventory(context: Context) -> Inventory:
    """
    Returns the inventory object in the given context.
    """
    return context["inventory"]


def get_scene_manager(context: Context) -> SceneManager:
    """
    Returns the scene manager object in the given context.
    """
    return context["scene_manager"]


def get_hotbar(context: Context) -> Hotbar:
    """
    Returns the hotbar object in the given context.
    """
    return context["hotbar"]


def get_message_box(context: Context) -> MessageBox:
    """
    Returns the message box object in the given context.
    """
    return context["message_box"]


def get_crop_window(context: Context) -> CropWindow:
    """
    Returns the crop window object in the given context.
    """
    return context["crop_window"]


def get_crop_grid(context: Context) -> Grid:
    """
    Returns the crop grid object in the given context.
    @returns: Grid[GameCrop | None]
    """
    return context["crop_grid"]
