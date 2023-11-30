"""
Inventory related functions.
"""
from src.core.context import Context
from src.world.context_getters import get_inventory
from src.world.item.inventory import Inventory


def init_inventory(context: Context) -> None:
    """
    Initializes the inventory.
    """
    context["inventory"] = Inventory(context)


def update_inventory(context: Context) -> None:
    """
    Updates the inventory.
    """
    get_inventory(context).update()
