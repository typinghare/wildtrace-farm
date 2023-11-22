"""
Map resource module.
"""
from src.registry import RegistryUtil
from src.world.data.registries import Registries
from src.world.map import Map, HouseMap, FarmMap


def register(path: str, _map: Map.__subclasses__()) -> Map.__subclasses__():
    """
    Register a map.
    :param path: The path of the map.
    :param _map: The map to register.
    :return: The map registered.
    """
    return Registries.Map.register(RegistryUtil.createRegistry(path), _map)


class Maps:
    """
    Maps.
    """

    House: HouseMap = register("house", HouseMap())
    Farm: FarmMap = register("farm", FarmMap())
