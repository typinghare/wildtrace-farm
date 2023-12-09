"""
Shopping module
"""
from typing import List

import pygame
from pygame import Vector2, Surface

from src.core.common import Size
from src.core.context import Context
from src.core.display import Layer
from src.world.common.constants import Fonts
from src.world.context_module import ContextModule
from src.world.data.products import Products
from src.world.item.product import Product
from src.world.util import get_font


class Shopping(ContextModule):
    """
    Shopping.
    """

    def __init__(self, context: Context):
        super().__init__(context)

        # Products
        self.products: List[Product] = [
            Products.WheatSeeds,
            Products.BeetSeeds,
            Products.CarrotSeeds,
            Products.CauliflowerSeeds,
            Products.EggplantSeeds,
            Products.PumpkinSeeds,
        ]

        # Border
        self.border: int = 10

        # Size
        screen_size = self.context.display.size
        self.size: Size = Size(screen_size.width * 0.8, self.border + 70 * len(self.products))

        # Layer
        self.layer: Layer = Layer(self.size)

        # Selected index
        self.selected_index: int = 0

        # Init
        self._init_layer()

    def _init_layer(self) -> None:
        """
        Initializes the layer.
        """
        self.context.display.set_layer("shopping", self.layer)

        screen_size = self.context.display.size
        self.layer.offset = Vector2(
            (screen_size.width - self.size.width) // 2,
            (screen_size.height - self.size.height) // 2,
        )

        self.layer.hidden = True

    def update(self) -> None:
        """
        Updates the shopping layer.
        """
        surface = self.layer.surface
        surface.fill(self.context.settings.inventory_background_color)
        slot_color = self.context.settings.inventory_slot_background_color
        selected_slot_color = self.context.settings.inventory_selected_slot_background_color

        font = get_font(36, Fonts.Manaspace)
        for row, product in enumerate(self.products):
            is_selected = row == self.selected_index

            row_surface = Surface((self.size.width - self.border * 2, 60), pygame.SRCALPHA)
            row_surface.fill(selected_slot_color if is_selected else slot_color)
            row_surface.blit(product.item.image, Vector2(6, 6))

            # blit product
            surface.blit(row_surface, Vector2(self.border, self.border + row * 70))

            # Name text
            name_text = font.render(product.item.name, True, "black")
            surface.blit(name_text, Vector2(self.border + 75, self.border + 12 + row * 70))

            # Price text
            price_str = str(product.price)
            price_text = font.render(f"${price_str}", True, "orange")
            surface.blit(
                price_text,
                Vector2(
                    surface.get_width() - self.border - 35 - 24 * (len(price_str)),
                    self.border + 14 + row * 70,
                ),
            )

    def move_down(self) -> None:
        """
        Selected index moves down.
        """
        self.selected_index = (self.selected_index + 1) % len(self.products)

    def move_up(self) -> None:
        """
        Selected index moves up.
        """
        self.selected_index = (self.selected_index - 1) % len(self.products)

    def open(self) -> None:
        """
        Opens the shopping window.
        """
        self.selected_index = 0
        self.layer.hidden = False

    def close(self) -> None:
        """
        Closes the shopping window.
        """
        self.layer.hidden = True

    def get_selected_product(self) -> Product:
        """
        Returns the selected product.
        """
        return self.products[self.selected_index]
