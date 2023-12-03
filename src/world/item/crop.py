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

    class Stage:
        """
        Crop stages.
        """

        Seedling = 0
        Vegetative = 1
        Budding = 2
        Ripening = 3

    def __init__(self, product: Product, image_list: List[Surface], days_to_ripe: int):
        # The product of this crop
        self.product: Product = product

        # The image (seedling(0) => vegetative(1) => budding(2) => ripening(3))
        self.image_list: List[Surface] = image_list

        # The number of days for this crop to ripe
        self.days_to_ripe: int = days_to_ripe

    def get_stage(self, day: int) -> int:
        """
        Returns the stage of a specified day.
        :param day: The given day.
        """
        if day >= self.days_to_ripe:
            return Crop.Stage.Ripening

        return int(day // (self.days_to_ripe / 3))


class GameCrop:
    """
    Game crop.
    """

    def __init__(self, crop: Crop):
        # Crop
        self.crop = crop

        # The current day of the crop
        self.day: float = 1

        # Whether the crop is watered today
        self.watered: bool = False

    @property
    def stage(self) -> int:
        return self.crop.get_stage(int(self.day))

    @property
    def image(self) -> Surface:
        return self.crop.image_list[self.stage]

    @property
    def stage_str(self) -> str:
        return [
            "Seedling",
            "Vegetative",
            "Budding",
            "Ripening",
        ][self.stage]
