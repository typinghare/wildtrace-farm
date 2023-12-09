"""
Crop item module.
"""
from src.registry import RegistryUtil
from src.world.data.crops import Crops
from src.world.data.items import Items
from src.world.data.registries import Registries
from src.world.item.crop import Crop
from src.world.item.crop_item import CropItem


def register(path: str, crop_item: CropItem) -> Crop:
    """
    Register a crop item.
    :param path: The path of the crop.
    :param crop_item: The crop item to register.
    :return: The crop item.
    """
    return Registries.CropItem.register(RegistryUtil.createLoc(path), crop_item)


class CropItems:
    """
    Crop item resources.
    """

    Wheat = register("wheat", CropItem(Items.WheatSeeds, Crops.Wheat))
    Beet = register("beet", CropItem(Items.BeetSeeds, Crops.Beet))
    Carrot = register("carrot", CropItem(Items.CarrotSeeds, Crops.Carrot))
    Cauliflower = register("cauliflower", CropItem(Items.CauliflowerSeeds, Crops.Cauliflower))
    Eggplant = register("eggplant", CropItem(Items.EggplantSeeds, Crops.Eggplant))
    Pumpkin = register("pumpkin", CropItem(Items.PumpkinSeeds, Crops.Pumpkin))
