"""
Crop module.
"""
from typing import List

from pygame import Surface

from src.world.item.product import Product


class Crop:
    """
    Crops are plants that are grown from seeds to be harvested for the purpose of profit.
    """

    def __init__(self, product: Product, image_list: List[Surface], days_to_ripe: int):
        # The product of this crop
        self.product: Product = product

        # The image (seedling(0) => vegetative(1) => budding(2) => ripening(3))
        self.image_list: List[Surface] = image_list

        # The number of days for this crop to ripe
        self.days_to_ripe: int = days_to_ripe

    def get_image(self, day: int) -> Surface:
        """
        Returns the image of a specified day.
        :param: day The given day.
        """
        if day >= self.days_to_ripe:
            # Return the ripening image
            return self.image_list[3]

        index = int(day // (self.days_to_ripe / 3))
        return self.image_list[index]


class GameCrop:
    """
    Game crop.
    """

    def __init__(self, crop: Crop):
        # Crop
        self.crop = crop
