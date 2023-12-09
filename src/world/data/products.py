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
    Carrot = register("carrot", Items.BeetProduct, 18)
    Cauliflower = register("cauliflower", Items.BeetProduct, 32)
    Eggplant = register("eggplant", Items.BeetProduct, 28)
    Pumpkin = register("pumpkin", Items.BeetProduct, 54)

    # Seeds
    WheatSeeds = register("seeds/wheat", Items.WheatProduct, 4)
    BeetSeeds = register("seeds/beet", Items.BeetProduct, 5)
    CarrotSeeds = register("seeds/carrot", Items.BeetProduct, 4)
    CauliflowerSeeds = register("seeds/cauliflower", Items.BeetProduct, 8)
    EggplantSeeds = register("seeds/eggplant", Items.BeetProduct, 9)
    PumpkinSeeds = register("seeds/pumpkin", Items.BeetProduct, 12)
