"""
Product resource module.
"""
from src.registry import RegistryUtil
from src.world.data.products import Products
from src.world.data.registries import Registries
from src.world.data.tiles import Tiles
from src.world.farm.crop import Crop


def register(path: str, crop: Crop) -> Crop:
    """
    Register an item.
    :param path: The path of the crop.
    :param crop: The crop to register.
    :return: The crop.
    """
    return Registries.Crop.register(RegistryUtil.createRegistry(path), crop)


class Crops:
    """
    Crop resources.
    """

    Wheat = register(
        "wheat",
        Crop(
            Products.Wheat,
            [
                Tiles.WheatSeedling,
                Tiles.WheatBudding,
                Tiles.WheatVegetative,
                Tiles.WheatRipening,
            ],
            6,
        ),
    )
    Beet = register(
        "beet",
        Crop(
            Products.Beet,
            [
                Tiles.BeetSeedling,
                Tiles.BeetBudding,
                Tiles.BeetVegetative,
                Tiles.BeetRipening,
            ],
            7,
        ),
    )
