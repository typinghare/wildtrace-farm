"""
Registries module.
"""

from src.registry import RegistryUtil


class Registries:
    """
    Registries.
    """

    TileSet = RegistryUtil.createRegistry("tile-set")
    Tile = RegistryUtil.createRegistry("tile")
    Sprite = RegistryUtil.createRegistry("sprite")

    EventListener = RegistryUtil.createRegistry("event-listener")
