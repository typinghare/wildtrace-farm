"""
Item resource modules.
"""
from src.registry import RegistryUtil
from src.world.data.registries import Registries
from src.world.data.tiles import Tiles
from src.world.item import Item


def register(path: str, item: Item) -> Item:
    """
    Register an item.
    :param path: The path of the item.
    :param item: The Item to register.
    :return: The animation.
    """
    return Registries.Frames.register(RegistryUtil.createRegistry(path), item)


class Items:
    """
    Item resources.
    """

    # Tools
    WateringCan = register("tool/watering_can", Item("Watering Can", Tiles.ToolWateringCan))
    Hoe = register("tool/hoe", Item("Hoe", Tiles.ToolHoe))

    # Seeds
    WheatSeeds = register("seeds/wheat", Item("Wheat Seeds", Tiles.WheatSeeds, 64))
    BeetSeeds = register("seeds/beet", Item("Beet Seeds", Tiles.BeetSeeds, 64))
