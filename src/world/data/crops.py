"""
Product resource module.
"""
from src.registry import RegistryUtil
from src.world.data.products import Products
from src.world.data.registries import Registries
from src.world.data.tiles import Tiles
from src.world.item.crop import Crop


def register(path: str, crop: Crop) -> Crop:
    """
    Register a crop.
    :param path: The path of the crop.
    :param crop: The crop to register.
    :return: The crop.
    """
    return Registries.Crop.register(RegistryUtil.createLoc(path), crop)


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
                Tiles.WheatVegetative,
                Tiles.WheatBudding,
                Tiles.WheatRipening,
            ],
            5,
        ),
    )
    Beet = register(
        "beet",
        Crop(
            Products.Beet,
            [
                Tiles.BeetSeedling,
                Tiles.BeetVegetative,
                Tiles.BeetBudding,
                Tiles.BeetRipening,
            ],
            7,
        ),
    )
