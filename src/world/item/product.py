"""
Product module.
"""
from src.world.item.item import Item


class Product:
    """
    Products are items that can be sold.
    """

    def __init__(self, item: Item, price: int):
        # The item
        self.item = item

        # The price of this product
        self.price: int = price
