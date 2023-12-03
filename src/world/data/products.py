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

    Wheat = register("wheat", Items.WheatProduct, 10)
    Beet = register("beet", Items.BeetProduct, 12)
