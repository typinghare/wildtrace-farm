"""
Context getters module. This module provides a bunch of utility functions that get a value from the
given context.
"""
from src.core.context import Context
from src.world.character import Character
from src.world.data_window import DataWindow


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
