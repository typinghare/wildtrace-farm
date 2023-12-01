"""
Crop item module.
"""
from src.world.item.crop import Crop
from src.world.item.item import Item


class CropItem:
    """
    Crop item.
    """

    def __init__(self, item: Item, crop: Crop):
        # item
        self.item: Item = item

        # crop
        self.crop: Crop = crop
