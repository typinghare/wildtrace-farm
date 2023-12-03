"""
Map resource module.
"""
from src.registry import RegistryUtil
from src.world.data.registries import Registries
from src.world.map import Map
from src.world.maps.home import HomeMap
from src.world.maps.farm import FarmMap


def register(path: str, _map: Map.__subclasses__()) -> Map.__subclasses__():
    """
    Register a map.
    :param path: The path of the map.
    :param _map: The map to register.
    :return: The map registered.
    """
    return Registries.Map.register(RegistryUtil.createLoc(path), _map)


class Maps:
    """
    Map resources.
    """

    Home: HomeMap = register("house", HomeMap())
    Farm: FarmMap = register("farm", FarmMap())
