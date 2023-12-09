"""
Product resource module.
"""
from src.registry import RegistryUtil
from src.world.data.items import Items
from src.world.data.registries import Registries
from src.world.item.product import Product
from src.world.item.item import Item


def register(path: str, item: Item, price: int) -> Product:
    """
    Register a product.
    :param path: The path of the product.
    :param item: The item of the product.
    :param price: The selling price of the product.
    :return: The product.
    """
    return Registries.Product.register(RegistryUtil.createLoc(path), Product(item, price))


class Products:
    """
    Product resources.
    """

    # Products
    Wheat = register("wheat", Items.WheatProduct, 16)
    Beet = register("beet", Items.BeetProduct, 22)
    Carrot = register("carrot", Items.CarrotProduct, 18)
    Cauliflower = register("cauliflower", Items.CauliflowerProduct, 32)
    Eggplant = register("eggplant", Items.EggplantProduct, 28)
    Pumpkin = register("pumpkin", Items.PumpkinProduct, 54)

    # Seeds
    WheatSeeds = register("seeds/wheat", Items.WheatSeeds, 4)
    BeetSeeds = register("seeds/beet", Items.BeetSeeds, 5)
    CarrotSeeds = register("seeds/carrot", Items.CarrotSeeds, 4)
    CauliflowerSeeds = register("seeds/cauliflower", Items.CauliflowerSeeds, 8)
    EggplantSeeds = register("seeds/eggplant", Items.EggplantSeeds, 9)
    PumpkinSeeds = register("seeds/pumpkin", Items.PumpkinSeeds, 12)
