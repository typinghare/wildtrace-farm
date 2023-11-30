"""
Context getters module. This module provides a bunch of utility functions that get a value from the
given context.
"""
from src.core.context import Context
from src.world.character import Character
from src.world.curtain import Curtain
from src.world.data_window import DataWindow
from src.world.item.inventory import Inventory


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
